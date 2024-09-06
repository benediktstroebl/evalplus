```python
def is_multiply_prime(a):
    primes = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37]
    factors = set(int(i) for i in range(1, a + 1) if a % i == 0)
    return not any(x in factors for x in primes)
```

The function `is_multiply_prime` checks if the number is the multiplication of three prime numbers. It first assumes the number's factors and then checks if any number in the list of primes is in the set of factors, if so, it returns false, if not, it returns true. 

This solution can be optimized, as it checks the factors of the number 'a' iteratively, which can lead to redundancy, hence it doesn't always yield a proper runtime for big 'a'.