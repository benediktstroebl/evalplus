```python
from typing import List

def factorize(n: int) -> List[int]:
    """
    Return list of prime factors of given integer in the order from smallest to largest.
    Each of the factors should be listed number of times corresponding to how many times it appears in factorization.
    Input number should be equal to the product of all factors

    Args:
        n (int): The number to factorize

    Returns:
        List[int]: A list of prime factors
    """
    factors = []
    i = 2
    while n > 1:
        # If n is divisible by i, then i is a factor
        if n % i == 0:
            # Add i to the factors list
            factors.append(i)
            # Divide n by i to remove this factor from n
            n = n // i
        else:
            # If i is not a factor, increment i by 1
            i += 1
    return factors

# Test cases
print(factorize(8))  # Output: [2, 2, 2]
print(factorize(25))  # Output: [5, 5]
print(factorize(70))  # Output: [2, 5, 7]
```

This script defines a function `factorize` that takes an integer `n` as input and returns a list of its prime factors. The function uses a simple trial division method to find the prime factors. It starts by checking if `n` is divisible by 2 (the smallest prime number), and if so, adds 2 to the list of factors and divides `n` by 2. This process is repeated until `n` is no longer divisible by 2. Then, the function increments the divisor by 1 and repeats the process until `n` is 1. The list of factors is returned at the end.