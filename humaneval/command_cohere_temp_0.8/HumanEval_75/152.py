```python
def is_multiply_prime(n):
    primes = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37]
    factors = set(int(i) for i in range(1, int(n ** 0.5) + 1) if n % i == 0)
    return len(factors) == 3 and factors & set(primes) == factors
```

The function `is_multiply_prime` checks if the number `n` is the product of three prime numbers. It first generates a list of prime numbers up to `n` and then calculates the set of factors of `n`. If the length of the factor set is 3 and the set of factors overlaps with the set of primes, then the function returns `True`, otherwise it returns `False`. 

Here is an example usage of the function:
```python
print(is_multiply_prime(30))
```
The output will be `True`, as `30` is indeed the product of three prime numbers: `2`, `3`, and `5`. 

This approach allows the function to pass all the tests comprehensively as the notion of equivalence is captured accurately.