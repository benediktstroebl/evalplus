### Prime Factorization Python Script

```python
from typing import List

def factorize(n: int) -> List[int]:
    """
    Return list of prime factors of given integer in the order from smallest to largest.
    Each of the factors should be listed number of times corresponding to how many times it appears in factorization.
    Input number should be equal to the product of all factors

    Args:
        n (int): The number to be factorized.

    Returns:
        List[int]: A list of prime factors of the input number.
    """
    i = 2
    factors = []
    while i * i <= n:
        if n % i:
            # If n is not divisible by i, increment i by 1
            i += 1
        else:
            # If n is divisible by i, append i to factors and divide n by i
            n //= i
            factors.append(i)
    # If n is a prime number greater than 1, append it to factors
    if n > 1:
        factors.append(n)
    return factors

# Example usage
print(factorize(8))  # Output: [2, 2, 2]
print(factorize(25))  # Output: [5, 5]
print(factorize(70))  # Output: [2, 5, 7]
```

This script uses a while loop to iterate through numbers from 2 to the square root of `n`. If `n` is divisible by the current number `i`, it appends `i` to the list of factors and divides `n` by `i`. If `n` is not divisible by `i`, it increments `i` by 1. Once the loop completes, if `n` is a prime number greater than 1, it appends `n` to the list of factors. The function then returns the list of factors.