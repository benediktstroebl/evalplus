```python
from typing import List

def factorize(n: int) -> List[int]:
    """ Return list of prime factors of given integer in the order from smallest to largest
    Each of the factors is listed number of times which corresponds to the number of times it appears in factorization of the number.
    """ For example, 8 = 2 x 2 x 2, so the result should be [2, 2, 2]
    """
    factors = []
    while n % 2 == 0:
        factors.append(2)
        n = n // 2
    for i in range(3, int(n**0.5) + 1, while n % i == 0:
        factors.append(i)
        n = n // i
    factors.append(int)
    n = n // int(n**0.5)
    final two, which is the largest prime factor.
``` 
Here's the markdown code block:
```
# Prime factorization

``` 
Let's take a test case, and if it passes, we will update the markdown content.