Here is a Python script with a self-contained function that solves the problem and passes corresponding tests:
```python
def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True
```

This function checks if a given number is prime or not. It first checks if the given number is less than 2, returning false immediately if so. It then iterates from 2 up to the square root of the number `n`, checking if the given number is divisible by any other number. If the number is divisible by any other number in this range, it returns false, indicating that the number is not prime. If the number is not divisible by any number in this range, it returns True, indicating that the number is prime. 

This algorithm, stopping at the square root of n, is an optimized version of the obvious check-all-factors approach, reducing the number of iterations necessary.

This function can be used to verify whether a number is prime or not. 

For example:
```python
>>> is_prime(6)
False
>>> is_prime(101)
True
>>> is_prime(11)
True
>>> is_prime(13441)
True
>>> is_prime(61)
True
>>> is_prime(4)
False
>>> is_prime(1)
False
```

These examples test cases that match the specification provided earlier.