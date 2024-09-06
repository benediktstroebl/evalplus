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
The function factorizes the input integer n and returns a list of its prime factors in order from smallest to largest. Each factor is listed number of times corresponding to how many times it appears in factorization. The function runs in O(n) time complexity, which is a very efficient algorithm for finding prime factors. 

This is a basic example of a Python function that can be used to solve a real-world problem, and can be a building block for more complex data structures and algorithms.