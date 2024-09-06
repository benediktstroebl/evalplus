```python
from typing import List
def factorize(n: int) -> List[int]:
    """ Return list of prime factors of given integer in the order from smallest to largest
    Each of the factors should be listed number of times which corresponds to how many times it appears in the factorization of the given number
    Input number should be equal to the product of all the factors returned
    """
    if n < 2:
        raise ValueError("Input number should be at least 2 or a positive integer")
    factors = []
    while n % 2 == 0:
        factors.append(2)
        n = n // 2
    for i in range(3, int(n ** 0.5) + 1, :
        while n % i == 0:
            factors.append(i)
            n = n // i
    for num in factors:
        if num > 1:
            nums = []
            while n % num == 0:
                nums.append(n)
                n = n // num
    return nums
```