### Factorize Function
```python
from typing import List

def factorize(n: int) -> List[int]:
    """
    Return list of prime factors of given integer in the order from smallest to largest.
    Each of the factors should be listed number of times corresponding to how many times it appears in factorization.
    
    Parameters:
    n (int): Input number.
    
    Returns:
    List[int]: List of prime factors.
    
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
    while n > 1:
        count = 0
        while n % i == 0:
            n = n // i
            count += 1
        if count > 0:
            factors.extend([i] * count)
        i += 1
    return factors
```

### Example Use Cases
```python
print(factorize(8))   # Output: [2, 2, 2]
print(factorize(25))  # Output: [5, 5]
print(factorize(70))  # Output: [2, 5, 7]
```

In this code, we use a while loop starting from 2 to check each number up to the square root of `n`. We use another while loop to divide `n` by the current factor as many times as possible, effectively getting the count of that factor. If the count is greater than 0, we extend the `factors` list with the factor repeated `count` times. We increment the current factor by 1 and repeat the process until `n` is reduced to 1.