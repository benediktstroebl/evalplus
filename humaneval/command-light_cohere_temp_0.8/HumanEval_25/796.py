```python
from typing import List
def factorize(n: int) -> List[int]:
    """ Return list of prime factors of given integer in the order from smallest to largest. """>
    numbers = [2, 3, 5, 7]
    for i in range(2, n // 2 + 1):
        is_prime = True
        for j in range(2, int(i ** 0.5) + 1):
            if n % j == 0:
                is_prime = False
                break
        if is_prime:
            numbers.append(i)
    return numbers
```