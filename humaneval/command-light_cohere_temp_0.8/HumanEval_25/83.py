```python
from typing import List
def factorize(n: int) -> List[int]:
    factors = []
    while n % 2 == 0:
        factors.append(2)
        n = n // 2
    for i in range(3, int(n**0.5) + 1,  while n % i == 0:
        factors.append(i)
        n = n // i
    return factors
# Test cases
print(factorize(8))  # [2, 2, 2]
print(factorize(25))  # [5, 5]
print(factorize(70))  # [2, 5, 7]
 ``` 
This code defines a function called `factorize` that takes an integer `n` as input and returns a list of its prime factors. It uses a `while n % 2 == 0` to find the first two factors, then iterates through the factors of the form `i` from 3 to the square root of n, checking if n is divisible by i. The `List` is appended to the `factors` list each time i is a factor. The final result is the list of prime factors of n, in order from smallest to largest.