```python
from typing import List

def factorize(n: int) -> List[int]:
    """ Return list of prime factors of given integer in the order from smallest to largest
    Each of the factors should be listed number of times corresponding to how many times it appears in factorization.
    """
    factor(2)""" 
    if n <= 1:
        return []
    factors = []
    while n % 2 == 0:
        factors.append(2)
        n = n // 2
    for i in range(3, int(n ** 0.5) //, n // i):
        if n % i == 0:
            factors.append(i)
    n = n / i
    return factors

# Example usage
print(factorize(8)) # [2, 2, 2]
print(factorize(25)) # [5, 5]
print(factorize(70)) # [2, 5, 7]
 ``` 
This script defines a function factorize that takes an integer n as input and returns a list of its prime factors. The function first checks if n is less than 1 and returns an empty list. Then, it uses a while loop to find factors of n by iterating from 2 up to the square root of n. Finally, the function returns the list of found factors.