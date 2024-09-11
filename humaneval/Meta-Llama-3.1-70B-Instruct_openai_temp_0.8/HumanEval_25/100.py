```python
from typing import List

def factorize(n: int) -> List[int]:
    """
    Return list of prime factors of given integer in the order from smallest to largest.
    Each of the factors should be listed number of times corresponding to how many times it appeares in factorization.
    Input number should be equal to the product of all factors

    Args:
        n (int): Input number to be factorized

    Returns:
        List[int]: List of prime factors of the input number
    """
    def _factorize(n: int, i: int = 2) -> List[int]:
        # Base case: if n is reduced to 1, return an empty list
        if n == 1:
            return []
        
        # If n is divisible by i, add i to the list and recurse with n // i
        if n % i == 0:
            return [i] + _factorize(n // i, i)
        
        # If n is not divisible by i, increment i and recurse
        return _factorize(n, i + 1)

    return _factorize(n)


# Test cases
print(factorize(8))   # [2, 2, 2]
print(factorize(25))  # [5, 5]
print(factorize(70))  # [2, 5, 7]
```

This script uses a recursive helper function `_factorize` to find the prime factors of the input number. The base case is when `n` is reduced to 1, at which point an empty list is returned. If `n` is divisible by `i`, `i` is added to the list and the function is called recursively with `n // i`. If `n` is not divisible by `i`, `i` is incremented and the function is called recursively again. The main function `factorize` simply calls the helper function and returns the result.