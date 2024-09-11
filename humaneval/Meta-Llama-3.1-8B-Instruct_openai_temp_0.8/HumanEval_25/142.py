### Factorization of an Integer
#### Problem Description
The task is to create a function `factorize(n)` that returns a list of prime factors of a given integer `n`. The list should contain each prime factor in the order from smallest to largest, and each factor should appear in the list as many times as its corresponding power in the factorization.

#### Solution

```python
from typing import List
import math

def factorize(n: int) -> List[int]:
    """
    Return list of prime factors of given integer in the order from smallest to largest.
    Each of the factors should be listed number of times corresponding to how many times it appears in factorization.
    
    Args:
    n (int): The input number to be factorized.

    Returns:
    List[int]: A list of prime factors of the input number.
    """
    factors = []
    for i in range(2, int(math.sqrt(n)) + 1):
        while n % i == 0:
            factors.append(i)
            n = n // i
    if n > 1:
        factors.append(n)
    return factors

# Example usage:
print(factorize(8))  # [2, 2, 2]
print(factorize(25))  # [5, 5]
print(factorize(70))  # [2, 5, 7]
```

#### How it works:
- The code starts by initializing an empty list `factors` to store the prime factors.
- It then iterates over numbers from 2 to the square root of the input number `n`.
- For each divisor `i` found, the code appends `i` to the `factors` list and divides `n` by `i` as many times as possible.
- If `n` is a prime number greater than 1, it is added to the `factors` list after the loop.
- Finally, the `factors` list is returned as the result.

This solution is efficient because it only divides `n` by each potential factor up to the square root of `n`, reducing the number of divisions required.