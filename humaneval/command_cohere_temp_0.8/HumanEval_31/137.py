```python
def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True
```

This function incorporates an optimized approach that checks only the divisibility of a number by integers up to its square root. Given the assumption that the number is larger than 1, if no such divisors are found, the number must be prime. 

This function may be tested with a markdown block providing a few test cases like the ones you've provided before:
```python
# Test the is_prime function
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

The expected output of each test case is provided within corresponding ">>> " blocks.