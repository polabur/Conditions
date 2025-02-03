# Ask the user for input
first_term = int(input("Enter first term number: "))
last_term = int(input("Enter last term number: "))


total_sum = 0
for num in range(first_term, last_term + 1):
    total_sum += num


print(f"\nThe sum of the numbers from {first_term} to {last_term} is {total_sum}")



# Ask the user for input
first_term = int(input("Enter first term number: "))
last_term = int(input("Enter last term number: "))


total_sum = 0
for num in range(first_term, last_term + 1):
    total_sum += num


print(f"\nThe sum of the numbers from {first_term} to {last_term} is {total_sum}")


# Ask the user for input
num = int(input("Enter a number: "))


if num > 1:
    is_prime = True 

 
    for i in range(2, num):
        if num % i == 0:
            is_prime = False  
            break  


    if is_prime:
        print(f"{num} is a prime number.")
    else:
        print(f"{num} is not a prime number.")
else:
    print(f"{num} is not a prime number.")  