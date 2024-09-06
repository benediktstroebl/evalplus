```python
from typing import List

def factorize(n: int) -> List[int]:
    """ Return list of prime factors of given integer in the order from smallest to largest.
    factorize = [x // evaluates to True
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            yield i
            while n % i == 0:
                n = n // i
    return [i for i in factorize]
    ```