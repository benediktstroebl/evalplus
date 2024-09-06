```python
from typing import List
def factorize(n):
    factors = []
    while n % 2 == 0:
        factors.append(2)
        n = n // 2
    while n > 1:
        if n % 3 == 0:
            factors.append(3)
        n = n // 3
        elif n % 5 == 0:
            factors.append(5)
        n = n // 5
        elif n % 7 == 0:
            factors.append(7)
        n = n // 7
        else:
            i = 6
            while i * 6 <= n:
                factors.append(i * 2**(i + 1))
                i += 1
            factors.append(int(n))
    return factors
#Test cases
print(factorize(8))  # [2, 2, 2]
print(factorize(25))  # [5, 5]
print(factorize(70))  # [2, 5, 7]
 ``` 
This script defines a function called `factorize` that takes an integer `n` as input and returns a list of its prime factors. The function uses a algorithm to factorize the number and returns the list of prime factors in order, starting with the smallest factor and continuing until the largest factor.