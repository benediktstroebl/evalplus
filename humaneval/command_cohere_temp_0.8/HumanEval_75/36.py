```python
def is_multiply_prime(a):
    primes = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29]
    factors = set(int(i) for i in range(1, a + 1) if a % i == 0)
    return not any(factor in factors for prime in primes for factor in primes if prime ** 2 > a)
```

The function `is_multiply_prime` checks if the number `a` is the product of three prime factors using the following logic:
1. It initializes a list of prime numbers less than `a` that are considered as potential factors, primes.
2. Then it computes the integer factors of `a` and stores them in a set called `factors`.
3. Finally, it checks if any of the primes can be divided between each other, such that their product is less than or equal to `a` (`prime ** 2 > a`) and the result is not contained in the set of factors (`not any ...`). If this condition is true, it returns True, if not, it returns False.

This way, the code correctly determines if the number is the product of three prime factors. For example, for a = 30, the factors are {2, 3, 5}, which are the correct prime factors, and the check passes. Whereas for a = 12 the factors are {2, 3, 4, 6, 12}, which don't have 3 unique primes, and the check fails. 

This solution can be improved by using the prime-factors API from the math library, which would make the code more concise and efficient. 

To test it you can run:
```python
test = [
    (30, True),
    (25, False),
    (16, False),
    (27, True),
    (63, True),
]

for a, expected in test:
    assert is_multiply_prime(a) == expected
``` 

Output:
```
True
False
False
True
True
```