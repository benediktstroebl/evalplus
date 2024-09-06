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

# Test cases
print(is_prime(6))  # Output: False
print(is_prime(101))  # Output: True
print(is_prime(11))  # Output: True
print(is_prime(13441))  # Output: True
print(is_prime(61))  # Output: True
print(is_prime(4))  # Output: False
print(is_prime(1))  # Output: False
```
This Python function checks whether a given number is a prime or not. It starts by checking numbers less than or equal to 2 and 3, then uses a while loop to check divisibility of numbers ranging from 5 up to the given number, finally returning True if the number is prime, and False otherwise.

It efficiently checks primality using a simple algorithm with minimal complexity. This function can be used as a standalone tool to determine whether a given number is prime.