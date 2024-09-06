```python
from typing import List

def factorize(n: int) -> List[int]:
    """ Return list of prime factors of given integer in the order from smallest to largest
    Each of the factors are listed number of times which corresponds to how many times it appears in the factorization of the number
    Input number should be a power of two (can be made even). Example: 25 = 5 * 5
    """
    if n < 2:
        return []

    # check even factorization
    temp = n // 2
    if temp in factorize(temp):
        return [temp] + factorize(temp)

    # check odd factorization
    odd_fac = []
    while n % 2 == 0:
        temp = n // 2
        odd_fac.append(temp)
        n = n // temp
    if n > 2:
        odd_fac.append(n)

    return odd_fac

# Test
print(factorize(25))
```