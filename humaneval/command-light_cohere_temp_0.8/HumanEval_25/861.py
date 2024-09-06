```python
from typing import List
def factorize(n: int) -> List[int]:
    factors = []
    while n % 2 == 0:
        factors.append(2)
        n = n // 2
    for i in range(3, int(n ** 0.5) + 1, while n % i == 0:
        factors.append(i)
        n = n // i
    factors.append(int(n))
    return factors
```
This function takes an integer `n` as input and returns a list of prime factors of `n` in order from smallest to largest. The function uses a `while` loop to check for divisibility by 2, 3, and so, and then uses a `for` loop to check for divisibility by numbers greater than the square root of `n`. The function also uses the `int()` function to convert the number to an integer data type.