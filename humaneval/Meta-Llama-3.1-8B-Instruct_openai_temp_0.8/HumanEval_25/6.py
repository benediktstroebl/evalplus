### Prime Factorization in Python
```markdown
### Prime Factorization Script

This script takes an integer as input and returns its prime factors, each listed in the order from smallest to largest.

### Code

```python
from typing import List

def factorize(n: int) -> List[int]:
    """
    Return list of prime factors of given integer in the order from smallest to largest.
    Each of the factors should be listed number of times corresponding to how many times it appears in factorization.
    
    Args:
    n (int): The input number to be factorized.

    Returns:
    List[int]: A list of prime factors of the input number.

    Examples:
    >>> factorize(8)
    [2, 2, 2]
    >>> factorize(25)
    [5, 5]
    >>> factorize(70)
    [2, 5, 7]
    """
    i = 2
    factors = []
    while i * i <= n:
        if n % i:
            i += 1
        else:
            n //= i
            factors.append(i)
    if n > 1:
        factors.append(n)
    return factors

# Example usage:
print(factorize(8))   # Output: [2, 2, 2]
print(factorize(25))  # Output: [5, 5]
print(factorize(70))  # Output: [2, 5, 7]
```

### Explanation

This script works by continuously dividing the input number `n` by the smallest prime factor, which is 2. If `n` is not divisible by 2, we increment the divisor by 1. This process continues until `n` is reduced to 1. The list of factors is constructed by appending the divisor whenever `n` is divided by it.

The time complexity of this script is O(sqrt(n)), where n is the input number. This is because we only need to check up to the square root of n to find its prime factors. The space complexity is O(sqrt(n)) as well, as in the worst case, we might need to store all the prime factors of n in the list.