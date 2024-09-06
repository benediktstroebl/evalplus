Here's a Python script with a self-contained function `is_prime` that solves the problem:
```python
def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True
```

This function checks if a given number is prime or not. It first checks if the given number is less than 2, returning `False` if so. Then, it iterates from 2 to the square root of the number, checking whether the number is divisible by any other number. If the number is divisible by any other number in this range, it returns `False`. However, if the number is not prime, it returns `True`.

Here's a snippet of tests to ensure its behavior matches the problem statement:
```python
# Tests:
assert is_prime(6) == False
assert is_prime(101) == True
assert is_prime(11) == True
assert is_prime(13441) == True
assert is_prime(61) == True
assert is_prime(4) == False
assert is_prime(1) == False
```