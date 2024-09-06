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

# Example usage:
print(is_prime(6))  # Output: False
print(is_prime(101))  # Output: True
print(is_prime(11))  # Output: True
print(is_prime(13441))  # Output: True
print(is_prime(61))  # Output: True
print(is_prime(4))  # Output: False
print(is_prime(1))  # Output: False
```
This code defines the `is_prime` function that checks if a given number is a prime or not, based on the primality testing algorithm explained above. The function uses an `if > 1` condition to skip some simple cases (numbers less than or equal to 1 and 2 and numbers that are multiples of 3), then checks divisibility by numbers of the form 5 (or 6) up to the square root of the input number. 
Finally, the function returns `True` if the number is prime and `False` otherwise.