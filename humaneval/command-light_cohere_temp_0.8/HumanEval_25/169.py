```python
from typing import List
def factorize(n: int) -> List[int]:
    """ Return list of prime factors of given integer in the order from smallest to largest
    """
    factors = []
    while n % 2 == 0:
        factors.append(2)
        n = n // 2
    for i in range(3, int(n**0.5) + 1, while n % i == 0:
        factors.append(i)
        n = n // i
    for num in range(int(n**0.25), 10):
        while n % num == 0:
        factors.append(num)
    return factors
```
The function first finds the smallest factor and keeps adding it and the number it divides by to get the next factor. The function checks if the numbers that can be divided by it, and adds it to the list of prime factors.