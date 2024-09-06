```python
from typing import List

def factorize(n: int) -> List[int]:
    factors = []
    while n % 2 == 0:
        factors.append(2)
        n = n // 2
    for i in range(3, int(n**0.5) + 1,):
        while n % i == 0:
            factors.append(i)
            n = n // i
    factors.append(n)
    return factors
```
The function 'factorize' in this script takes an integer 'n' as input and returns a list of its prime factors in ascending order. It employs the loop to factorize the input number by locating its factors and returning them in order from the smallest to the largest.

The function also handles the edge case of input being a prime number by returning a list containing only that number. 

Feel free to use this solution to solve the problem of finding prime factors of a given number in markdown code blocks.