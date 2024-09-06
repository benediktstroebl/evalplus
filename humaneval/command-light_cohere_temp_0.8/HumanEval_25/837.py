```python
from typing import List

def factorize(n: int) -> List[int]:
    """ Return list of prime factors of given integer in the order from smallest to largest.
    n = int(input()) # taking input from the user.
    factors = []
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            factors.append(i)
            n //= i
        factors.append(n)
    return factors
```
The function takes an integer **n** as input and returns a list of prime factors of **n** in the order from smallest to largest. The function checks if the current number is divisible by the current factor.  It appends the to the list of factors if the current number is divisible by the current factor.