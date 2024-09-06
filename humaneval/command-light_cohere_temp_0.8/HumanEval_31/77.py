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

This Python function checks whether a given number is prime or not. It uses a basic primality rules and checks if the number meets any of the following conditions:
1. If the number is less than or equal to 1, it returns False, indicating that the number is not prime.
2. If the number is 2 or 3, it returns True since both numbers are prime.
3. If the number is divisible by 2 or 3, it returns False.
4. If the number starts with 6, it checks if the number is divisible by any integer less than or equal to the square root of the number.
5. If the number satisfies any conditions, it returns True, indicating that the number is prime.

This function can be used to quickly determine whether a given number is prime or not, which can be useful in various algorithms and applications.