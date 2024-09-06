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
```
The function `factorize` is designed to return a list of prime factors of a given integer `n`. The function utilizes a while loop and an `append` function to continuously add the factors until the number is divided by a prime number. The function also accounts for the numbers that are less than the square root of the number, and in such cases, it utilizes another while loop to handle the factors correctly. The function ensures that the output is in order from smallest to largest, which is the expected behavior for the prime factorization of an integer.