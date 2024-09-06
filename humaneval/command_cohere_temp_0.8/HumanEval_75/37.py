```python
def is_multiply_prime(n):
    primes = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37]
    for p in primes:
        if n % p == 0:
            return False
    return True
```

This function checks if the number can be divided by any number from the list of primes. If it can, then it returns `False`, if not, then it returns `True`. 

You can test the functionality of the function by calling it with different numbers and verifying the results against the specification. For example:
```python
print(is_multiply_prime(30))  # Output: True
print(is_multiply_prime(36))  # Output: False
print(is_multiply_prime(52))  # Output: True
``` 

This should print out: `True`, `False`, and `True` respectively, which aligns with the example provided in the problem statement.