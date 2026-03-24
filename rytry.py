import math

def is_prime(n):
    """Checks if a number is prime."""
    if n <= 1:
        return False
    # Check for factors up to the square root of n
    for i in range(2, int(math.sqrt(n)) + 1):
        if (n % i) == 0:
            return False
    return True

# Get the range from the user
try:
    a = int(input("Enter start of range: "))
    b = int(input("Enter end of range: "))
except ValueError:
    print("Invalid input. Please enter valid integers for the range.")
    exit()

even_count = 0
odd_count = 0
even_sum = 0
odd_sum = 0
non_prime_numbers = []

# Ensure the starting number is less than or equal to the ending number
if a > b:
    a, b = b, a # Swap if necessary

# Iterate through the range of numbers
for num in range(a, b + 1):
    # Check for even/odd and calculate counts and sums
    if num % 2 == 0:
        even_count += 1
        even_sum += num
    else:
        odd_count += 1
        odd_sum += num

    # Check for non-prime numbers
    if not is_prime(num):
        non_prime_numbers.append(num)

# 
print(f"\nResults for the range [{a}, {b}]:")
print(f"Even count: {even_count}")
print(f"Odd count: {odd_count}")
print(f"Even sum: {even_sum}")
print(f"Odd sum: {odd_sum}")
print("Non-prime numbers in this range:", non_prime_numbers)
