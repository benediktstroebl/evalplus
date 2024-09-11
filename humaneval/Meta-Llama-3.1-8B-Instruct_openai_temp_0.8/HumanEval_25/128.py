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
        List[int]: A list of prime factors of the input number.
    """
    factors = []
    i = 2
    while n > 1:
        # If n is divisible by i, then it is a factor
        if n % i == 0:
            # Count the occurrences of i in the factorization
            count = 0
            while n % i == 0:
                count += 1
                n //= i
            # Append the factor and its count to the list
            factors.extend([i] * count)
        else:
            # If n is not divisible by i, increment i
            i += 1
    return factors

# Test cases
print(factorize(8))  # [2, 2, 2]
print(factorize(25))  # [5, 5]
print(factorize(70))  # [2, 5, 7]
```

This script uses a while loop to check each number from 2 up to the square root of the input number `n`. If `n` is divisible by the current number `i`, then `i` is a factor of `n`. The script counts the occurrences of `i` in the factorization by repeatedly dividing `n` by `i`. The factor and its count are then appended to the list of factors. If `n` is not divisible by the current number `i`, then the script increments `i` and continues checking. This process continues until `n` is reduced to 1.