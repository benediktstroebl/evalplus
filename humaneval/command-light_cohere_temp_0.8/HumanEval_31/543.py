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

This function uses a simple algorithm to check if a given number is prime or not. The function first handles a numbers less than or equal to 1, which are clearly prime. It then checks for numbers less than or equal to 3, as these numbers have no divisors less than or equal to their square root. It then iterates up numbers starting from 5, and checks if the given number is divisible by any of these numbers or their sum and difference (i.v numbers which are divisors of the given number).