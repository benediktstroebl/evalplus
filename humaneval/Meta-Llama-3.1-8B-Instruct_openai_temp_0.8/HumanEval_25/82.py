### Code
```markdown
from typing import List
import math

def factorize(n: int) -> List[int]:
    """
    Return list of prime factors of given integer in the order from smallest to largest.
    Each of the factors should be listed number of times corresponding to how many times it appears in factorization.
    Input number should be equal to the product of all factors

    Args:
        n (int): The number to factorize

    Returns:
        List[int]: List of prime factors
    """
    factors = []
    i = 2
    while i * i <= n:
        if n % i:
            i += 1
        else:
            n //= i
            factors.append(i)
    if n > 1:
        factors.append(n)
    return factors

# Test cases
print(factorize(8))  # [2, 2, 2]
print(factorize(25))  # [5, 5]
print(factorize(70))  # [2, 5, 7]
```
### Explanation

This script uses a simple trial division method to find the prime factors of a given number. It starts by dividing the input number `n` by the smallest prime number, which is 2. If `n` is divisible by 2, it divides `n` by 2 and adds 2 to the list of factors. This process is repeated until `i` (the number we're trying to divide `n` by) is greater than the square root of `n`. At this point, `n` is guaranteed to be a prime number, so we add it to the list of factors.

This approach ensures that the list of factors is in the correct order (from smallest to largest) and that each factor appears the correct number of times. The time complexity of this algorithm is O(√n), which is acceptable for relatively small input values. For larger input values, more efficient algorithms may be necessary.