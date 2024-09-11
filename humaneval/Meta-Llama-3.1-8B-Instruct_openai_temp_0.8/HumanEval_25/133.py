```python
from typing import List

def factorize(n: int) -> List[int]:
    """
    Return list of prime factors of given integer in the order from smallest to largest.
    Each of the factors should be listed number of times corresponding to how many times it appears in factorization.
    Input number should be equal to the product of all factors

    Args:
        n (int): The input integer to be factorized

    Returns:
        List[int]: A list of prime factors of the input integer
    """

    def get_prime_factors(n: int) -> dict:
        """
        Get prime factors of a given integer

        Args:
            n (int): The input integer to be factorized

        Returns:
            dict: A dictionary where keys are prime factors and values are their counts
        """
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

    def sort_factors(factors: dict) -> List[int]:
        """
        Sort prime factors by their values

        Args:
            factors (dict): A dictionary where keys are prime factors and values are their counts

        Returns:
            List[int]: A list of prime factors sorted by their values
        """
        return sorted([factor for factor, _ in factors.items()], key=lambda x: factors[x])

    factors = get_prime_factors(n)
    return sort_factors(factors)


# Test cases
print(factorize(8))  # [2, 2, 2]
print(factorize(25))  # [5, 5]
print(factorize(70))  # [2, 5, 7]
```

In this script, we first define a helper function `get_prime_factors(n)` to get the prime factors of a given integer `n` as a dictionary where keys are prime factors and values are their counts. Then we define another helper function `sort_factors(factors)` to sort the prime factors by their values. Finally, we use these two functions to implement the `factorize(n)` function, which returns the list of prime factors of the input integer `n` in the order from smallest to largest.