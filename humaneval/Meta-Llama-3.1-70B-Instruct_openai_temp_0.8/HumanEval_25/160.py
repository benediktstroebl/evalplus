```python
from typing import List
import math

def factorize(n: int) -> List[int]:
    """
    Return list of prime factors of given integer in the order from smallest to largest.
    Each of the factors should be listed number of times corresponding to how many times it appeares in factorization.
    Input number should be equal to the product of all factors
    
    :param n: Input number to be factorized
    :return: List of prime factors
    """
    factors = []
    for i in range(2, int(math.sqrt(n)) + 1):
        while n % i == 0:
            factors.append(i)
            n = n // i
    if n > 1:
        factors.append(n)
    return factors

# Test cases
print(factorize(8))  # [2, 2, 2]
print(factorize(25))  # [5, 5]
print(factorize(70))  # [2, 5, 7]
```
This script uses a simple trial division method to find the prime factors of a given number. It iterates through numbers from 2 to the square root of the input number, and checks if the current number is a factor. If it is, the number is divided by the factor and the factor is added to the list. This process is repeated until the number is fully factorized. If the remaining number is greater than 1, it means it is a prime factor and it is also added to the list.