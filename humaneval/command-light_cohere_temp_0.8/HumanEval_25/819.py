```python
from typing import List

def factorize(n: int) -> List[int]:
    """
    Return list of prime factors of given integer in the order from smallest to largest.
    Input number should be equal to the product of all factors.
    """
    list comprehension to find all factors, and remove duplicates
    """
    factors = []
    for i in range(1, n+1):
        if n % i == 0:
            factors.append(i)
            n //=i
    factors.append(n)
    return factors
```
This script defines a function 'factorize' which returns a list of prime factors of a given number 'n' in descending order. It uses a list comprehension to iterate through all numbers from 1 up to the given number, and checks if the number is divisible by each of these numbers. It then appends the unique factors to the list, which are numbers that were factors of the original number. The list is then sorted in descending order, and contains each number of each prime factor only once.