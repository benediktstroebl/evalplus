### Prime Factorization Script
```python
from typing import List


def factorize(n: int) -> List[int]:
    """
    Return list of prime factors of given integer in the order from smallest to largest.
    Each of the factors should be listed number of times corresponding to how many times it appears in factorization.
    Input number should be equal to the product of all factors
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
        if n % i:
            i += 1
        else:
            n //= i
            factors.append(i)
    if n > 1:
        factors.append(n)
    return factors


# Example usage:
if __name__ == "__main__":
    print(factorize(8))  # [2, 2, 2]
    print(factorize(25))  # [5, 5]
    print(factorize(70))  # [2, 5, 7]
```

### Explanation

This script uses a simple trial division method to find the prime factors of a given integer. The `factorize` function takes an integer `n` as input and returns a list of its prime factors in the order from smallest to largest.

Here's a step-by-step breakdown of how it works:

1. Initialize an empty list `factors` to store the prime factors.
2. Initialize a variable `i` to 2, which is the smallest prime number.
3. Loop until `i` squared is greater than `n` (the input number).
4. Inside the loop, check if `n` is divisible by `i`. If not, increment `i` by 1.
5. If `n` is divisible by `i`, divide `n` by `i` and append `i` to the `factors` list.
6. Repeat steps 3-5 until `i` squared is greater than `n`.
7. If `n` is greater than 1 after the loop, it means that `n` is a prime number, so append it to the `factors` list.
8. Return the `factors` list.

The example usage at the end of the script demonstrates how to use the `factorize` function with some sample inputs.