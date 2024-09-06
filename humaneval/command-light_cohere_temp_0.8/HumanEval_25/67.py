```python
from typing import List

def factorize(n: int) -> List[int]:
    """ Return list of prime factors of given integer in the order from smallest to largest.
    # Initialize aarray of factors as empty list.
    factors = []
   
    # Iterate through 2 to sqrt(n) and check if n is divisible by the product of i and ith prime
    # factor.
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            factors.append(i)
            factors.append(i * int(n / i))
    factors.append(i)
    return factors
```
This function factorsizes a given number `n` by returning a list of its prime factors. The function starts by initializing an empty list called `factors`. It then iterates through the numbers from 2 up to the square root of `n`, and checks if `n` is divisible by the product of the current prime factor `i` and the current `i`th prime `j`. If `n` is divisible by the product of `i` and `j`, it append both `i` and `j` to the `factors` list, and also append the product of `i` and `n` divided by `i` to the `factors` list. The function then returns the the list.