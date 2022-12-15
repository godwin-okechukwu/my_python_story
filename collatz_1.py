
n = int(input("Enter a positive number: "))
count = 0 

while n > 1:
        if n % 2 == 0:
                n = n // 2
        else: 
                n = n * 3 + 1
        print(n, end=" ")
        count += 1

print("\nThat sequence has ", + count, " terms")

	


	




    
