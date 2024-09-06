Here is a Python script that defines a function `greatest_common_divisor` solving the problem of finding the greatest common divisor of two integers `a` and `b`:

```python
def greatest_common_divisor(a: int, b: int) -> int:
    if not a or not b:
        return 0

    # Find the prime factorization of a and b
    pa = power(prime_factors(a),[0]))
    pb = power(prime_factors(b),[0])

    # Find the greatest common divisor of the prime factors
    gcd = max(pa[i] for i, x in enumerate(pa) if pb[i] == x)

    return gcd

def prime_factors(n: int) -> List[int]:
    factors = []
    divisor = 2
    while not n % divisor:
        factors.append(divisor)
        n //= divisor
    factors.append(n)
    return factors
```

This script defines a function that calculates the greatest common divisor of two integers, `a` and `b`, by finding the largest divisor of their prime factors. The function takes two integers as input and returns the greatest common divisor.

The `prime_factors` function is used to generate the prime factors of a given integer. It works by iteratively dividing the number by each number from 2 up until it becomes a whole number. The function returns a list of the prime factors.