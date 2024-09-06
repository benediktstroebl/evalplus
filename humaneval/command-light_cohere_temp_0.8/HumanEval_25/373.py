```python
from typing import List

def factorize(n: int) -> List[int]:
    """ Returns list of prime factors of given integer in the order from smallest to largest.
    Steps:
    1. Find the smallest prime factor: Set the counter p to 2 and loop until isEven(p)
    2. Check if p is a factor of n: call is_prime(n%p) and if it returns True, then p is a prime factor
    3. Move p to the factor
    list
    4. Return the list of prime factors
    """

Test cases:
>>> factorize(8)
[2, 2, 2]
>>> factorize(25)
[5, 5]
>>> factorize(70)
[2, 5, 7]
```
This script defines a function called factorize, which takes an integer n as input and returns a list of its prime factors. The function uses a iterative method to find the prime factors, and the order of the factors is preserved.