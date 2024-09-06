Here's a Python script with a self-contained function that solves the problem and passes corresponding tests:
```python
def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True
```

This function checks if a given number is prime or not. It first checks if the number is less than 2, returning `False` if so. Then, it iterates from 2 up to the square root of the number, checking whether the number is divisible by any other number. If the number is divisible by any other number in this range, it returns `False`. However, if the number is not divisible by any number in this range, it returns `True`, indicating that the number is prime. 

This approach is efficient as it only requires checking divisors up to the square root of the number. Primes are the only numbers that don't have any divisors beyond their square root. 
```python
# Test the function
assert is_prime(6) == False
assert is_prime(101) == True
assert is_prime(11) == True
assert is_prime(13441) == True
assert is_prime(61) == True
assert is_prime(4) == False
assert is_prime(1) == False
```

This test suite covers a variety of scenarios to ensure that the `is_prime` function performs according to expectations. 
This way, you can verify the correctness of the function against various inputs.