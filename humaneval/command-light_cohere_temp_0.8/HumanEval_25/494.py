```python
from typing import List
def factorize(n: int) -> List[int]:
    """ Return list of prime factors of given integer in the order from smallest to largest
    Each of the factors are listed number of times corresponding to how many times it appears in factorization
    Input number should be equal to the product of all the factors
    """
    if n < 2:
        return []
    factors = []
    while n % 2 == 0:
        factors.append(2)
        n = n // 2
    for i in range(3, int(n**0.5) + 1, while n % i == 0:
        factors.append(i)
        n = n // i
    for i in range(int(n**0.5) + 1):
        if n % i == 0:
            factors.append(i)
    return factors
```

This function takes an integer `n` as input and returns a list of prime factors of `n`, ordered from smallest to largest. The function first determines if `n` is less than 2, and if so, returns an empty list. Then, it performs a loop that continuously divides `n` by 2 until the remainder becomes non-zero, and at each division, adds the divisor to the list of factors. Finally, it performs another loop that checks divisibility of `n` with each prime numbers from 3 to the square root of `n`, and adds the divisor as a factor to the list of factors if the check is successful.