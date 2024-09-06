```python
from typing import List
def factorize(n: int) -> List[int]:
    """ Return list of prime factors of given integer in the order from smallest to largest.
    ``` Each of the factors should be listed number of times corresponding to how many times it appeases in factorization.
    Input number should be equal to the product of all factors
    """
    factors = []
    while n % 2 == 0:
        factors.append(2)
        n = n // 2
    for i in range(3, int(n**0.5) + 1, while n % i == 0:
        factors.append(i)
        n = n // i
    for j in range(int(n**0.5) + 1):
        if n % j == 0:
            factors.append(j)
    return factors
```
This Python code defines a function called `factorize` that takes an integer `n` as input and returns a list of prime factors of the given number. The function uses a basic algorithm to find the prime factors, starting with 2 and then checking for divisibility by numbers from 3 up until the square root of the input number. It uses the list comprehension to build the list of prime factors.