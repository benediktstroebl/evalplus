```python
from typing import List

def factorize(n: int) -> List[int]:
    """ Returns list of prime factors of given integer in the order from smallest to largest
    """
    factors = []
    while n % 2 == 0:
        factors.append(2)
        n = n // 2
    for i in range(3, int(n**0.5) + 1,):
        while n % i == 0:
            factors.append(i)
            n = n // i
    if n > 2:
        factors.append(n)
    return factors
```
The function 'factorize' uses a loop to find the prime factors of a given integer. It starts with the loop and adds the factors to the factors list when the number is not divisible by 2 or when it is divisible by all numbers from 3 to the square root of the input number.