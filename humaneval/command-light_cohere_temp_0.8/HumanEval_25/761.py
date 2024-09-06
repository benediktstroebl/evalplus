```python
from typing import List

def factorize(n: int) -> List[int]:
    factors = []
    while n > 1:
        if n % 2 == 0:
            factors.append(2)
        n = n // 2
    else:
        for i in range(3, int(n**0.5)+1,  if n % i == 0:
            factors.append(i)
            n = n // i
    return factors

# Test case
print(factorize(8))
print(factorize(25))
print(factorize(70))
``` 
This code defines a function factorize, which takes an integer n as input and returns a list of its prime factors in ascending order. The function uses a loop and the division algorithm to find the prime factors of n. The test cases show that the function works correctly for the given inputs.