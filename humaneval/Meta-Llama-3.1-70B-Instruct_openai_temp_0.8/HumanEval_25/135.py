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
        List[int]: A list of prime factors in the order from smallest to largest.
    """
    def is_prime(num: int) -> bool:
        """
        Check if a number is prime.

        Args:
            num (int): The number to be checked.

        Returns:
            bool: True if the number is prime, False otherwise.
        """
        if num < 2:
            return False
        for i in range(2, int(num ** 0.5) + 1):
            if num % i == 0:
                return False
        return True

    factors = []
    for i in range(2, n + 1):
        while n % i == 0 and is_prime(i):
            factors.append(i)
            n //= i
    return factors

# Example use cases:
print(factorize(8))  # [2, 2, 2]
print(factorize(25))  # [5, 5]
print(factorize(70))  # [2, 5, 7]
```

This script defines a function `factorize` that takes an integer `n` as input and returns a list of its prime factors in the order from smallest to largest. The function uses a helper function `is_prime` to check if a number is prime.

Here's a step-by-step explanation of how the script works:

1.  The `is_prime` function checks if a number is prime by iterating from 2 to the square root of the number and checking if it is divisible by any of these numbers.
2.  The `factorize` function starts by initializing an empty list `factors` to store the prime factors of the input number `n`.
3.  It then iterates from 2 to `n` (inclusive) and checks if `n` is divisible by the current number `i`. If `n` is divisible by `i` and `i` is prime (checked using the `is_prime` function), `i` is appended to the `factors` list and `n` is divided by `i`.
4.  The loop continues until `n` is reduced to 1, at which point all prime factors have been found and added to the `factors` list.
5.  Finally, the `factorize` function returns the `factors` list, which contains the prime factors of the input number in the order from smallest to largest.