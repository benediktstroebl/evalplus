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
    List[int]: A list of prime factors of the given number.
    """

    def prime_factors(n: int) -> List[int]:
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

    return prime_factors(n)


# Test cases
print(factorize(8))  # [2, 2, 2]
print(factorize(25))  # [5, 5]
print(factorize(70))  # [2, 5, 7]
```

In this script, we define a helper function `prime_factors` that finds the prime factors of a given number. It starts by dividing the number by the smallest prime number, which is 2, and continues dividing by the smallest prime numbers until the number is reduced to 1. The prime factors are then returned as a list.

The `factorize` function simply calls the `prime_factors` function and returns the result.

Note that this script uses a trial division method, which is not the most efficient method for large numbers. However, it is simple and easy to understand, and it works well for small to medium-sized numbers.