class PDA:
    def __init__(self):
        # Defining states and stack alphabet
        self.states = ['q0', 'q1', 'q2']
        self.start_state = 'q0'
        self.accepting_states = ['q0']

        # The stack that simulates the PDA's stack memory
        self.stack = []

    def process_string(self, input_string):
        current_state = self.start_state
        self.stack = []  # Reset stack for each new string

        # Process each symbol in the input string
        for symbol in input_string:
            if symbol not in ['(', ')']:
                raise ValueError("Input string contains invalid symbols.")

            if current_state in ['q0', 'q1']:
                if symbol == '(':
                    self.stack.append('(')
                    current_state = 'q1'
                elif symbol == ')':
                    if not self.stack:  # No '(' to match
                        return False
                    self.stack.pop()
                    if not self.stack:
                        current_state = 'q0'

        # Check if the string ends in accepting state and the stack is empty
        return current_state in self.accepting_states and not self.stack


# Create an instance of PDA
pda = PDA()


test_strings = ["()", "(()))", "(()())", "())", "(()", ")("]

for test_string in test_strings:
    result = pda.process_string(test_string)
    print(f"Input: {test_string} -> {'Accepted' if result else 'Rejected'}")
