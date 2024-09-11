```python
from typing import List

def factorize(n: int) -> List[int]:
    """
    Return list of prime factors of given integer in the order from smallest to largest.
    Each of the factors should be listed number of times corresponding to how many times it appeares in factorization.
    Input number should be equal to the product of all factors

    Args:
    n (int): The input number to factorize.

    Returns:
    List[int]: A list of prime factors in the order from smallest to largest.
    """
    def is_prime(num: int) -> bool:
        """
        Helper function to check if a number is prime.

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
    for i in range(2, n + 1):
        # Check if i is a factor of n
        while n % i == 0:
            # Check if i is prime
            if is_prime(i):
                # If i is prime, add it to the list of factors
                factors.append(i)
            # Divide n by i
            n = n // i
    return factors

# Test cases
print(factorize(8))     # [2, 2, 2]
print(factorize(25))    # [5, 5]
print(factorize(70))    # [2, 5, 7]
```