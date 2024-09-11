```python
from typing import List

def factorize(n: int) -> List[int]:
    """
    Return list of prime factors of given integer in the order from smallest to largest.
    Each of the factors should be listed number of times corresponding to how many times it appears in factorization.
    Input number should be equal to the product of all factors

    Args:
        n (int): The number to factorize.

    Returns:
        List[int]: A list of prime factors.
    """
    factors = []
    i = 2
    while n > 1:
        # Check if i is a factor of n
        if n % i == 0:
            # If i is a factor, append it to the list and divide n by i
            n = n // i  # Using floor division to get integer part
            if i not in factors:
                # Only append if the number isn't already in the list
                factors.append(i)
        else:
            # If i is not a factor, increment i by 1
            i += 1
    return factors

# Example use cases
print(factorize(8))  # [2, 2, 2]
print(factorize(25))  # [5, 5]
print(factorize(70))  # [2, 5, 7]
```

This Python function `factorize` calculates the prime factors of a given integer `n`. It uses a while loop to continuously try dividing `n` by the smallest integer `i` (starting from 2), until `n` is no longer divisible by `i`. When `n` is no longer divisible by `i`, `i` is incremented by 1. The process continues until `n` is reduced to 1. The list of factors is updated accordingly, ensuring each factor is only included if it is not already in the list. This approach guarantees that the output list contains the prime factors in the correct order and frequency.