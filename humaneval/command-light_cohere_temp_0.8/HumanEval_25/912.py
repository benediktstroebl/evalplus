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
    factors.append(int(n))
    return factors

# Test cases goes here...
```
The code defines a function `factorize` that calculates and returns a list of prime factors for a given integer `n`. The function utilizes a loop to factorize the number by dividing by 2 repeatedly until the number becomes odd, then it checks for divisibility with numbers from 3 up to the square root of the original number. The function then appends each found factor to the `factors` list. The function also handles the last case, where the number is a perfect square, and returns the square itself as a prime factor. 

It provides a self-contained function with test cases to solve the problem.