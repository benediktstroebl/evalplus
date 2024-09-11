```python
from typing import List

def factorize(n: int) -> List[int]:
    """
    Return list of prime factors of given integer in the order from smallest to largest.
    Each of the factors should be listed number of times corresponding to how many times it appeares in factorization.
    Input number should be equal to the product of all factors

    Args:
        n (int): The input number to be factorized.

    Returns:
        List[int]: A list of prime factors in the order from smallest to largest.
    """
    def is_prime(num: int) -> bool:
        """
        Check if a number is prime.

        Args:
            num (int): The number to check.

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

# Test cases
print(factorize(8))   # [2, 2, 2]
print(factorize(25))  # [5, 5]
print(factorize(70))  # [2, 5, 7]
```

This script first defines a helper function `is_prime` to check if a number is prime. However, for the purpose of factorization, we don't actually need this helper function. We can directly check if `n` is divisible by `i` in the `while` loop.

In the `factorize` function, we start from 2 and keep dividing `n` by `i` as long as it is divisible. If `n` is not divisible by `i`, we increment `i` by 1. If `n` is a prime number greater than 1 at the end of the loop, we append it to the `factors` list.

The script then includes some test cases to verify the correctness of the `factorize` function.