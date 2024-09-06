Here's a Python script with a self-contained function `is_prime(n)` that solves the problem:
```python
def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True
```

This function checks if a given number is prime or not. It first checks if the number is less than 2, returning `False` if so. Then, it iterates from 2 to the square root of the number, checking for divisibility. If the number is divisible by any integer in that range, it returns `False`. If it is not, it returns `True`.

This code includes the expected test cases mentioned earlier, allowing you to verify the function's behavior against the specified cases. You can add additional test cases or further customize the script as needed. 
```python
# Tests
assert is_prime(6) == False
assert is_prime(101) == True
assert is_prime(11) == True
assert is_prime(13441) == True
assert is_prime(61) == True
assert is_prime(4) == False
assert is_prime(1) == False
```