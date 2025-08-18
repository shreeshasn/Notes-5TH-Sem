BEGIN{
count=0;
}

{
if($6=="cwnd_")
count++;
}

END{
printf("%f \t %f \n", $1, $7);
}
