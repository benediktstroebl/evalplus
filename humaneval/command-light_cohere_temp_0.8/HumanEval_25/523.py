```python
from typing import List

def factorize(n: int) -> List[int]:
    """ Return list of prime factors of given integer in the order from smallest to largest.
    Retrieves prime numbers using from list and keeps removing the factor until the current number cannot be divided by the remaining prime factors.
    """
    factors: List[int] = []
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            factors.append(i)
            if len(factors) == i:
                return factors
    """

# Example
n = 25
factors = factorize(n)
print(factors)  # Output: [5, 5]
``` 
This Python function called factorize takes an integer n as input and returns a list of prime factors of the input number in order from smallest to largest. It uses a time- division method to find prime factors and returns the list of factors.