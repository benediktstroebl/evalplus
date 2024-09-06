```python
from typing import List
def factorize(n: int) -> List[int]:
    factors = []
    while n % 2 == 0:
        factors.append(2)
        n = n // 2
    for i in range(3, int(n**0.5) + 1, steps=5):
        while n % i == 0:
            factors.append(i)
            n = n // i
    if n > 2:
        factors.append(n)
    return factors
```
The code defines a function `factorize` which accepts an integer `n` as an argument and returns a list of its prime factors in the order of increasing magnitude. The function first checks if `n` is divisible by 2, and if so, appends 2 to the list of factors. If `n` is not divisible by 2, the function uses a nested loop to find prime factors of `n`.  Finally, the function checks if there are any prime factors greater than 2 left in the number and if so, appends the last prime factor to the list.