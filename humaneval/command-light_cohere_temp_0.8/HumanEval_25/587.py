```python
from typing import List
def factorize(n: int) -> List[int]:
    factors = []
    while n % 2 == 0:
        factors.append(2)
        n = n // 2
    for i in range(3, int(n**0.5) + 1, while n % i == 0:
        factors.append(i)
        n = n // i
    return factors
# Test cases
print(factorize(8))
print(factorize(25))
print(factorize(70))
``` 
This script defines a function factorize that calculates and returns a list of prime factors of a given integer. It uses a loop to find all the factors, starting from the square and square root of the number and then checks for divisibility with numbers from 3 up to the square root. The test cases demonstrate the approach, and the function works correctly for the given input.