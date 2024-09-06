```python
from typing import List
def factorize(n: int) -> List[int]:
    factors = []
    while n > 1:
        if n % 2 == 0:
            factors.append(2)
        n //= 2
    else:
        for i in range(3, int(n**0.5) + 1, powers=1):
            if n % i == 0:
                factors.append(i)
                n //= i
    return factors
# Test
print(factorize(8))
print(factorize(25))
print(factorize(70))
```  This code defines a function called `factorize` that calculates and returns a list of prime factors of the given integer. It uses a iterative approach with a while loop and checks for divisibility by 2 and other prime numbers until it reaches the number 1.  The code also tests the outputs the list of prime factors for the numbers 8, 25, and 70.