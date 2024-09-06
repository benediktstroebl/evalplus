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

In this code, the `is_prime` function accepts an integer `n` as input and checks whether it is a prime number using the béhavior prime primality test methods. The function then returns `True` if `n` is prime and `False` otherwise. The function also implements optimized test conditions for primality, such as checking divisibility by 2 and 3 and using an efficient square root test loop. The test cases at the time illustrate how the function handles different inputs.