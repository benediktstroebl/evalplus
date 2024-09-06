```python
from typing import List

def factorize(n: int) -> List[int]:
    """ Return list of prime factors of given integer in the order from smallest to largest
    Each of the factors is listed number of times corresponding to how many times it appears in factorization
    Input number should be a product of all its factors
    """
    factors = []
    while n > 1:
        count = 0
        for i in range(2,int(n**.5) + 1):
            if n % i == 0:
                count += 1
                n = n // i
        if count == 0:
            factors.append(n)
            else:
                break
    return factors

# Test cases
print(factorize(8))  # [2, 2, 2]
print(factorize(25))  # [5, 5]
print(factorize(70))  # [2, 5, 7]
```
This code defines a function called factorize that takes an integer n as input and returns a list of its prime factors. The function uses a approach of finding factors by dividing by smaller numbers until the number becomes 1, and then backtracking to find the factors.