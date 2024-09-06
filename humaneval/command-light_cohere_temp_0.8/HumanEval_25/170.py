```python
from typing import List

def factorize(n: int) -> List[int]:
    """ Returns list of prime factors of given integer in the order from smallest to largest.
    Each of the factors should be listed number of times corresponding to how many times it appears in factorization.
    Input number should be equal to the product of all factors
    """
    factors = []
    while n % 2 == 0:
        factors.append(2)
        n = n // 2
    for i in range(3, int(n**0.5) + 1, while n % i == 0:
        factors.append(i)
        n = n // i
    factors.append(n)
    return factors

# Test cases
test_1 = factorize(8)
print(test_1)
test_2 = factorize(25)
print(test_2)
test_3 = factorize(70)
print(test_3)
```
The code defines a function called `factorize` that takes an integer `n` as input and returns a list of prime factors of the given number. The function uses a iterative approach to find the prime factors, checking divisibility by 2, 3, 5, 7, and numbers ending with 5 until the original number.