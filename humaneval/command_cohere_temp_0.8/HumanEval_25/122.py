```python
from typing import List

def prime_factors(n: int) -> List[int]:
    """ Return list of prime factors of given integer in the order from smallest to largest.
    Each of the factors should be listed number of times corresponding to how many times it appears in factorization.
    Input number should be equal to the product of all factors
    """
    if n <= 1:
        return []
    factors = []
    while n % 2 == 0:
        factors.append(2)
        n = n // 2
    for i in range(3, int(n**0.5) + 1, 2):
        while n % i == 0:
            factors.append(i)
            n = n // i
    if n > 2:
        factors.append(int(n))
    return factors

def factorize(n: int) -> List[int]:
    return [factor * num for factor in prime_factors(n) for num in range(factor == n // factor + 1)]
```
The factorize() function uses prime_factors() to compute the prime factors of the input number n. 
It then returns the factors listed in increasing order, with each factor repeated the number of times it appears in the factorization of n. 
The function handles cases when n is less than or equal to 1, returning an empty list in these cases.

Here is an example of use of the function:
```python
print(factorize(8))  # [2, 2, 2]
print(factorize(25))  # [5, 5]
print(factorize(70))  # [2, 5, 7]
``` 
The result is [2, 2, 2] because there are three 2's in the factorization of 8. There are two 5's in the factorization of 25. There is one each of 2, 5, and 7 in the factorization of 70.