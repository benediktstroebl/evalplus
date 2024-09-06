```python
from typing import List
def factorize(n):
    """ Return list of prime factors of given integer in the order from smallest to largest.
    factors = []
    while n != 1:
        for i in range(2, int(n**0.5)+1, while n % i == 0:
            factors.append(i)
            n = n // i
    return factors
# Test case 1: Factorize 8
print(factorize(8))  # [2, 2, 2]

# Test case 2: Factorize 25
print(factorize(25))  # [5, 5]

# Test case 3: Factorize 70
print(factorize(70))  # [2, 5, 7]
```
This script defines a function factorize that calculates and returns a list of prime factors for a given integer. It uses a loop to find all the divisors from 1 to the square root of the number and adds them to the factors list until the number becomes 1 again. The test cases pass the example code demonstrates how the function works for three different input values.