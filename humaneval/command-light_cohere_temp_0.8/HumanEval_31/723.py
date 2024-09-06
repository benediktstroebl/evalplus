```python
def is_prime(n):
    if n <= 1:
        return False
    if n <= 3:
        return True
    if n % 2 == 0 or n % 3 == 0:
        return False
    i = 5
    while i * i <= n:
        if n % i == 0 or n % (i + 2) == 0:
            return False
        i += 6
    return True

# Test the function
print(is_prime(6))  # Output: False
print(is_prime(101))  # Output: True
print(is_prime(11))  # Output: True
print(is_prime(13441))  # Output: True
print(is_prime(61))  # Output: True
print(is_prime(4))  # Output: False
print(is_prime(1))  # Output: False
``` 
The function 'is_prime' accepts an integer 'n' as input and outputs a boolean indicating whether 'n' is a prime number or not. 

The function begins by verifying that the input number is greater than or equal to 1. It then determines whether the specific conditions for prime numbers are met: namely, if the number is less than or equal to 2 or 3, it is a prime number. 

If none of these conditions are met, the function moves on to a loop that checks if the square of the number is less than or equal to the input number. It then verifies if the particular conditions are met for divisibility: if the number is divisible by 2, 3, or their sum (6). 

If the conditions are met, the function returns 'False', indicating that the number is not prime. If none of these conditions are met, the function returns 'True', indicating that the number is prime.