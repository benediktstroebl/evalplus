### Self-contained Python Script

```python
from typing import List

def factorize(n: int) -> List[int]:
    """
    Return list of prime factors of given integer in the order from smallest to largest.
    Each of the factors should be listed number of times corresponding to how many times it appears in factorization.
    Input number should be equal to the product of all factors
    
    Args:
        n (int): Input integer to be factorized.
        
    Returns:
        List[int]: A list of prime factors of given integer.
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

# Test cases
print(factorize(8))  # [2, 2, 2]
print(factorize(25))  # [5, 5]
print(factorize(70))  # [2, 5, 7]
```

This Python script implements the `factorize` function, which takes an integer `n` as input and returns a list of its prime factors in the order from smallest to largest. The function works by continuously dividing the input number `n` by the smallest divisor `i` until `n` is reduced to 1. If `n` is not divisible by `i`, `i` is incremented by 1. The function uses a `while` loop to repeatedly divide `n` by `i` and append `i` to the list of factors until `n` is reduced to 1. Finally, if `n` is greater than 1 after the loop, it means `n` is a prime number, and it is appended to the list of factors.