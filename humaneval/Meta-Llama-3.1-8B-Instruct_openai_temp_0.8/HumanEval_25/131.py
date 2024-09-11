```python
from typing import List

def factorize(n: int) -> List[int]:
    """
    Return list of prime factors of given integer in the order from smallest to largest.
    Each of the factors should be listed number of times corresponding to how many times it appears in factorization.
    Input number should be equal to the product of all factors

    Args:
        n (int): Number to be factorized

    Returns:
        List[int]: List of prime factors
    """
    def prime_factors(n: int) -> dict:
        """ Helper function to find prime factors of a number """
        i = 2
        factors = {}
        while i * i <= n:
            if n % i:
                i += 1
            else:
                n //= i
                factors[i] = factors.get(i, 0) + 1
        if n > 1:
            factors[n] = factors.get(n, 0) + 1
        return factors

    factors = prime_factors(n)
    return [key for key in factors.keys() for _ in range(factors[key])]


# Test cases
print(factorize(8))  # [2, 2, 2]
print(factorize(25))  # [5, 5]
print(factorize(70))  # [2, 5, 7]
```

In this script, the `factorize` function first uses a helper function `prime_factors` to find the prime factors of the input number and their counts in a dictionary. It then creates a list of these factors by iterating over the dictionary keys and values, repeating each key as many times as its corresponding value.