```python
from typing import List

def factorize(n: int) -> List[int]:
    """
    Return list of prime factors of given integer in the order from smallest to largest
    Each of the factors are listed number of times corresponding to how many times it appears in factorization
    Input number should be equal to the product of all its factors.
    """
   
    biggest number that can be factorized is first, then the next biggest divisor, and so on.
    """
    number = n // factorize_list = []
    while n % 1 == 0:
        n = n // 1
        factorize_list.append(n)

    return [n] + factorize_list
```