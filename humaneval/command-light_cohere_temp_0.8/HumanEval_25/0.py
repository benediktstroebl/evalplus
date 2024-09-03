```python
from typing import List

def factorize(n: int) -> List[int]:
    """
    Return list of prime factors of given integer in the order from smallest to largest.
    Each of the factors should be listed number of times corresponding to how many times it appeares in factorization.
    Input number should be equal to the product of all factors
    """
    factors = []
    while n % 2 == 0:
        factors.append(2)
        n //= 2
    for i in range(3, int(n ** 0.5) // :
        if n % i == 0:
            factors.append(i)
            n //= i
    factors.append(n)
    return factors
```
This Python function called `factorize` takes an integer `n` as input and returns a list of its prime factors in order from smallest to largest. It does this by iterating through numbers from 2 up until the square root of the input number, checking if the input number is divisible by each of these numbers. If it is, the number is divided by that factor, and that factor is added to the list of factors.