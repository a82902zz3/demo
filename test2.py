def reverse(s):
	reverse_string = ""
	for string in s[-1::-1]:
		reverse_string+=string
	return reverse_string
	
string =" i am so hHHHandsome guy !!!"
string_list = string.split()

for index in range(len(string_list)):
    string_list[index] = reverse(string_list[index])
		       
print(string_list)		       

print(" ".join(string_list))
		       
