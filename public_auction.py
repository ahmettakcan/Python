auction = {
	
}

again = "yes" 
while again == "yes":
	
	c = input("Enter your Name : ")
	d = int(input("Enter your Offer : "))
	
	auction[c] = d	
	again = input("Any other bidders? : ")

val = (list(auction.values()))
dict = list(auction.values())
key = (list(auction.keys()))

val.sort()
i = len(val) - 1
pos = dict.index(val[i])

print(f"All offer : {auction}")
print(f"{key[pos]} is won")
