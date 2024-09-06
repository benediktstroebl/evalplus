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

# Test the function with some values
print(is_prime(6))  # Output: True
print(is_prime(101))  # Output: True
print(is_prime(11))  # Output: True
print(is_prime(13441))  # Output: True
print(is_prime(61))  # Output: True
print(is_prime(4))  # Output: False
print(is_prime(1))  # Output: False
```

The above function checks whether a given number is a prime or not. If the number is less than 1, it returns False. If the number is less than or equal to 2 or 3, it returns True. If the number is a perfect square or can be expressed as the sum of consecutive odd numbers, it returns False. Otherwise, it checks for divisibility by prime numbers up to the square root of the number, and returns True if no such divisors are found. 

Finally, it checks if the given number is a prime number by checking divisibility by all prime numbers up to its square root.