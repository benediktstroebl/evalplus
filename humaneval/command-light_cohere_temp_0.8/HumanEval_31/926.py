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
The function is_prime checks whether a given number is prime or not. If the number is less than 1, it returns False. If the number is 2 or 3, it returns True immediately. If the number is a perfect square or can be expressed as 6k ± 1, where k is a positive integer, it returns False. If the number does not satisfy any of these conditions, it iterates up to the square root of the number, checking for divisibility by small squares and odd numbers. The function eventually returns True for prime numbers and False for non-prime numbers.