```python
def is_prime(n):
    """Returns True if the number is prime, and False otherwise."""
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

# Test cases
print(is_prime(6))  # Output: False
print(is_prime(101))  # Output: True
print(is_prime(11))  # Output: True
print(is_prime(13441))  # Output: True
print(is_prime(61))  # Output: True
print(is_prime(4))  # Output: False
print(is_prime(1))  # Output: False
```
This function checks whether a given number is prime or not. It uses a method that is based on the trial and error approach, where it tries to divide the number by numbers from 2 to the square root of the number, and checks for divisibility. The function also uses the numbers that are likely to be prime, such as 5, 7, and their multiples, as well as numbers that are the square root of their multiples.