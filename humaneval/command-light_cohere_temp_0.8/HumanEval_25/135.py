```python
from typing import List

def factorize(n: int) -> List[int]:
    """ Return list of prime factors of given integer in the order from smallest to largest
    Each of the factors is listed number of times corresponding to how many times it appears in factorization
    Input number should be equal to the product of all factors
    """
    factors = []
    while n % 2 == 0:
        factors.append(2)
        n = n // 2
    for i in range(3, int(n**0.5) + 1, while n % i == 0:
        factors.append(i)
        n = n // i
    for num in factors:
        nums = []
        while n % num == 0:
            nums.append(n)
            n = n // num
        factors.append(nums)
    return factors
```

This function calculates and returns the list of prime factors of the given number, following the algorithm from the question.