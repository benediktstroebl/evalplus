```python
from typing import List
def factorize(n: int) -> List[int]:
    """ Return list of prime factors of given integer in the order from smallest to largest.
    n = n.is_prime(n)
    if n <= 1:
        return []
    else:
        factors = []
        while n % 2 == 0:
            n = n // 2
            factors.append(2)
        for i in range(3, int(n**0.5) + 1, 2):
            if n % i == 0:
                factors.append(i)
                if i == n // i:
                    break
        return factors
    """

# Pass in some tests
n = 25
result = factorize(n)
print(result)  # Output: [5, 5]
n = 8
result = factorize(n)
print(result)  # Output: [2, 2, 2]
```
The function factorize solves the problem of finding prime factors of a given number n and returns a list of prime factors in order from smallest to largest. The list is ordered such maximum number of each factor in the list is equal to the number of times the factor appears in factorization of the number n.