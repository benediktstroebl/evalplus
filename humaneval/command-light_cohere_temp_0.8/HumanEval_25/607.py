```python
from typing import List

def factorize(n: int) -> List[int]:
    """ Returns list of prime factors of given integer in the order from smallest to largest. Each of the factors should be listed number of times corresponding to how many times it appears in factorization.
    Input number should be equal to the product of all factors"""

    factors = []
    while n % 2 == 0:
        factors.append(2)
        n = n // 2
    while n > 1:
        factor = int(n ** 0.5)
        n // 5
        factors.append(factor)
   
    factors.append(n)

    return factors
```
This script defines a function '**`factorize`**' that takes an integer '**`n`**' as input and returns a list of its prime factors. The function uses a while and a while loop, where it repeatedly divides '**`n`**' by 2 and adds the result to the list of factors if the division results in even. It also checks for other prime numbers using the formula **'**`n **⁵5`** and adds the prime factor to the list of factors.