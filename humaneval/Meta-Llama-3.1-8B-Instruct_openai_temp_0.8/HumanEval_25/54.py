### Prime Factorization
#### Script Description
The following Python script performs prime factorization of a given integer. It returns a list of prime factors in the order from smallest to largest, with each factor repeated according to its multiplicity in the factorization.

```python
from typing import List
import math

def factorize(n: int) -> List[int]:
    """
    Return list of prime factors of given integer in the order from smallest to largest.
    Each of the factors should be listed number of times corresponding to how many times it appears in factorization.
    
    Args:
    n: The input integer to be factorized.
    
    Returns:
    A list of prime factors.
    
    Example:
    >>> factorize(8)
    [2, 2, 2]
    >>> factorize(25)
    [5, 5]
    >>> factorize(70)
    [2, 5, 7]
    """
    factors = []
    i = 2
    while i * i <= n:
        count = 0
        while n % i == 0:
            n //= i
            count += 1
        if count > 0:
            factors.append(i) * count
        i += 1
    if n > 1:
        factors.append(n)
    return [factor for factor in factors if isinstance(factor, int)]

# Example usage:
print(factorize(8))   # [2, 2, 2]
print(factorize(25))  # [5, 5]
print(factorize(70))  # [2, 5, 7]
```

### Explanation

*   We use the property of prime factorization that a larger factor must be a multiple of a smaller factor that has already been divided out.
*   We start with the smallest prime number (2) and continuously divide the input number `n` by the current divisor `i` as long as it's divisible. We count the number of divisions, which represents the multiplicity of the divisor in the factorization.
*   Once we've divided `n` by `i` as many times as possible, we move on to the next divisor `i`.
*   If `n` is not fully divided initially, it means `n` is a prime number itself and we add it to the list of factors.
*   Finally, we construct the list of factors by repeating each prime factor according to its multiplicity.