```python
def is_prime(n):
    """ Returns true if the number is prime, and false otherwise. """
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
This code defines a `is_prime` function that checks whether a given number is prime or not. It employs various algorithms to determine primality, such as checking divisibility by 2 and 3, as well as trial and error with divisors within a given range. The output of this tests show that the function correctly identifies prime and non-prime numbers.