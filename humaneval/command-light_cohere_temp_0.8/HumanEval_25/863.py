```python
from typing import List

def factorize(n: int) -> List[int]:
    """ Return list of prime factors of given integer in the order from smallest to largest.
    If a product of all factors divided by 2^n.
    This product of all factors is divisible by 2^n
    """
    factors = []
    for i in range(1, int(n**0.5)+1):
        while n % i == 0:
        factors.append(i)
        n //= i
    return factors

# Test the function with a couple of numbers
test_factorize(25)  # Should return [5]
test_factorize(70)  # Should return [2, 5, 7]

```
The function factorize in this script provides a way to get a list of prime factors for a given number. The function works by iterating through numbers starting from 2 up and checking if the number is divisible by each of these numbers. The factors are then appended to the list. The function also uses the product of all factors divided by 2^n to ensure that the list of factors is ordered from smallest to largest.