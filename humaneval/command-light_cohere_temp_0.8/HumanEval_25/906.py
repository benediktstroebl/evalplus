```python
from typing import List
def factorize(n: int) -> List[int]:
    """Return list of prime factors of given integer in the order from smallest to largest
    Each of the factors is listed number of times which corresponds to how many times it appears in factorization of the number
    Input number should be equal to the product of all the factors returned
    """
    if n <= 1: return []
    factors = []
    while n % 2 == 0:
        factors.append(2)
        n = n // 2
    i = 3
    while i * i <= n:
        if n % i == 0:
            factors.append(i)
            n = n // i
        i += 1
    if n > 2: factors.append(n)
    return factors
```
The function 'factorize' accepts an integer 'n' as input and outputs a list of prime factors of 'n' in descending order, along with the number of occurrences of each factor. The function employs a following method:
1. Begin with a loop from 2 to the square root of 'n'. Within the loop, it checks whether 'n' is divisible by the current prime 'i'.
2. If 'n' is divisible by 'i', add 'i' to the list of factors.
3. If 'n' is not divisible by any prime less than or equal to its square root, append 'n' to the list of factors.

4. Return the list of prime factors.

5: Test cases: 
- Test case 1: Input number = 8
- Output: [2, 2, 2]
- Test case 2: Input number = 25
- Output: [5, 5]
- Test case 3: Input number = 70
- Output: [2, 5, 7]

This script is self-contained and can be used as-is to solve the problem.