```python
from typing import List

def factorize(n: int) -> List[int]:
    """
    Return list of prime factors of given integer in the order from smallest to largest.
    Each of the factors should be listed number of times corresponding to how many times it appears in factorization.
    Input number should be equal to the product of all factors.
    """
   
    can also be a small integer, or a large number that doesn't fit into memory.
    """
    can you general integer
    """
    if n < 0:
        return []
    elif n <= 1:
        return []
    else:
        factors = []
        while n % 2 == 0:
            n /= 2
            factors.append(2)
        else:
            for i in range(3, int(n**.5) + 1, step=5):
                if n % i == 0:
                    factors.append(i)
                    n //= i
            return factors
    return []
```