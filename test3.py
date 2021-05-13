number = 15
number_list = [n for n in range(0, number+1)]

count = 0	
		       
for n in number_list[1::]:
    
    if n%15 == 0 :
        count += 1
    elif n%3 == 0 or n % 5 == 0:
	   continue
    else  :
        count += 1
     
print(count)