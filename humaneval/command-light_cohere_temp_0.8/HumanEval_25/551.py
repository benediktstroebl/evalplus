```python
from typing import List

def factorize(n: int) -> List[int]:
    factors = []
    while n % 2 == 0:
        factors.append(2)
        n = n // 2
    while n > 1:
        for d in range(3, int(n**.5) + 1, by=2):
            if n % d == 0:
                factors.append(d)
                n = n // d
    factors.append(int(n))
    return factors
``` 
The function `factorize` calculates and returns a list of prime factors of the given number `n` in ascending order. It iterates through loop to find factors, removing even numbers first, and then testing the numbers from 3 to the square root of n. 

This function follows the mathematical definition of finding prime factors, and it is designed to be self-contained, with all the logic for finding prime factors in one function.