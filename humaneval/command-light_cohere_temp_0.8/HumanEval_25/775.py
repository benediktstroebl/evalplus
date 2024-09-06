```python
from typing import List

def factorize(n: int) -> List[int]:
    """ Returns list of prime factors of given integer in the order from smallest to largest.
    If input number is the product of all factors"""
    factors = []
    while n % 2 == 0:
        n //= 2
        factors.append(2)
    while n % 3 == 0:
        n //= 3
        factors.append(3)
    while n % 5 == 0:
        n //= 5
        factors.append(5)
    while n % 7 == 0:
        n //= 7
        factors.append(7)
    while not n:
        for i in range(2, int(n**0.5) + 1):
            if n % i == 0:
                factors.append(i)
                n //= i
    return factors

# Test case 1
print(factorize(8))
# Test case 2
print(factorize(25))
# Testcase3
print(factorize(70))
```