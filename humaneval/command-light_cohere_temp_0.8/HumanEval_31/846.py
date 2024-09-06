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

The Python function `is_prime(n)` determines whether a given number is a prime or not. The function initially determines whether the number is less than or equal to one and returns `False` if it is. Then, it checks for divisibility by 2 and 3 and returns `False` if the number is divisible by either of them. After that, it checks if the number is of the form `5^6k+1` and returns `False` if it is. Finally, it checks if the number is less than the square root of the number and returns `False` if it is. If none of these above conditions apply, the number is considered prime and the function returns `True`.