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
        List[int]: A list of prime factors.
    """
    def is_prime(num: int) -> bool:
        """
        Helper function to check if a number is prime.

        Args:
            num (int): The number to be checked.

        Returns:
            bool: True if the number is prime, False otherwise.
        """
        if num < 2:
            return False
        for i in range(2, int(num**0.5) + 1):
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
print(factorize(8))   # Expected output: [2, 2, 2]
print(factorize(25))  # Expected output: [5, 5]
print(factorize(70))  # Expected output: [2, 5, 7]
```
This script defines a function `factorize` that takes an integer `n` and returns a list of its prime factors. The function uses a helper function `is_prime` to check if a number is prime, although in this case it's not strictly necessary since we're only checking divisibility up to the square root of `n`. The main function iterates over numbers from 2 to the square root of `n`, dividing `n` by each number that divides it evenly and adding that number to the list of factors. Finally, if `n` is greater than 1 at the end of the loop, it's added to the list of factors (since it must be a prime number).