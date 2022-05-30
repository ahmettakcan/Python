alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

convert = input("Encypt or Decyrpt : ")

str = input("Write your password : ")

n = int(input("Write number : "))

def encypt(str ,n):
	strn = ""
	i, j = 0, 0
	length = len(str)
	
	while i < length:
		while j < 26:
			if str[i] == alphabet[j]:
				max = (j + n) % 26 
				strn += alphabet[max]
			j += 1
		j = 0
		i += 1
	print(strn)
def decrypt(str, n):
	strn = ""
	i, j = 0, 0
	length = len(str)

	while i < length:
		while j < 26:
			if str[i] == alphabet[j]:
				max = (j - n) % 26 
				strn += alphabet[max]
			j += 1
		j = 0
		i += 1
	print(strn)

if convert.lower() == "e":
	encypt(str, n)
  
elif convert.lower() == "d":
	decrypt(str, n)

answer = input("Would you like to continiue : ")
while answer == "yes":
	convert = input("Encypt or Decyrpt Again : ")
	str = input("Write your password again my honey : ")
	n = int(input("Write number again my love : "))
  
if convert.lower() == "e":
	encypt(str, n)
    
elif convert.lower() == "d":
	decrypt(str, n)
	  
answer = input("Would you like to continiue : ")
  
if answer == "no":
	print("Byeee! :(")
