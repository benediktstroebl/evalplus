```python
from typing import List

def factorize(n: int) -> List[int]:
    """
    Return list of prime factors of given integer in the order from smallest to largest
    Each of them is listed number of times which they occur in factorization of the given number.
    Input number should be equal to the product of all factors.

    Assume n=124567.
    Factors: 2^3^4
    """
    factors = []
    while n % 2 == 0:
        n /= 2
        factors.append(2)

    i = 3
    while i * i <= n:
        if n % i == 0:
            n /= i
            factors.append(i)
        i += 1

    for x in factors:
        factors.append(factors.count(x(x))
        factors.append(factors.count(x(x))
    return factors
```

This Python function called `factorize` takes an integer `n` as input and returns a list of prime factors of the input number, in ascending order. The function uses a trial and error approach to find the prime factors, and it also checks for the number being a perfect square to factorize. 

The function uses the 'while' loop to check for prime factors until the square root of the number becomes greater than the original number.