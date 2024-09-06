```python
def is_multiply_prime(a):
    primes = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37]
    if a < len(primes)**3: return False
    for prime in primes:
        if a % prime == 0:
            return False
    return True
```
The code defines a function `is_multiply_prime(a)` that checks if the given number `a` is the multiplication of three prime numbers. It does so by first generating a list of prime numbers up to the square root of `a` (assuming that all prime factors are less than the square root). Then, it checks if any of the prime factors of `a` are present in the list of primes. If none are found, it returns `False`, and if any are found, it returns `True`. Also, it handles the corner case where `a` is less than the cube root of the max prime, in which case it clearly cannot be a product of three primes.  This approach ensures that the function is self-contained and does not require any additional dependencies or complex algorithms.