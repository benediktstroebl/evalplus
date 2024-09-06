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

This Python function, `is_prime()`, determines whether a given number is a prime. The function first determines if the number is less than or equal to 1 and returns `False` in such cases. It then determines if the prime is less than or equal to 3 and returns `True` since primes are of odd numbers. The function then checks for the divisibility of the number by 2 and 3, returning `False` if the number is divisible by either of these numbers. 

The function then initializes a counter `i` to 5 and while `i` times `i` does not exceed the number, the function checks if the number is divisible by `i` or `i + 2`. If so, it returns `False`. Otherwise, the function increments `i` by 6 and repeats the process until `i` exceeds the given number.  The if the is a prime number, it returns `True`.