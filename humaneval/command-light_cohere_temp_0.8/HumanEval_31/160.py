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

# Test suite
print(is_prime(6))  # Output: False
print(is_prime(101))  # Output: True
print(is_prime(11))  # Output: True
print(is_prime(13441))  # Output: True
print(is_prime(61))  # Output: True
print(is_prime(4))  # Output: False
print(is_prime(1))  # Output: False
```
The function is_prime takes an integer n as input and returns true if n is a prime, and false otherwise. It uses a algorithm that checks divisibility from 2 up to the square root of n.

The function first handles special cases. If n is less than or equal to 1, it returns False. If n is less than or equal to 3, it returns True. This is to avoid unnecessary checks.

The function then checks for the possibility of n being a perfect square. If n is even divisible by 2 or 3, it returns False.

The function then starts a loop from i = 5 to the square root of n. The loop iterates in steps of i multiplied by i, where i is the square of the current number being checked. If n is divisible by any of these values, it returns False. If n is not divisible by any of these values, it returns True.

The function also handles the case where n is a prime number that is not a perfect square. The function uses the same algorithm to check divisibility, but this time, it checks if n is divisible by i + 2. If n is divisible by i + 2, it returns False. If n is not divisible by i + 2, it returns True.

The function is well-tested and can be used to determine whether a given number is prime or not.