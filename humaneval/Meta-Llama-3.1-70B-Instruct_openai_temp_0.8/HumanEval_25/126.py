```python
from typing import List

def factorize(n: int) -> List[int]:
    """
    Return list of prime factors of given integer in the order from smallest to largest.
    Each of the factors should be listed number of times corresponding to how many times it appeares in factorization.
    Input number should be equal to the product of all factors
    """
    def is_prime(num: int) -> bool:
        """Check if number is prime."""
        if num < 2:
            return False
        for i in range(2, int(num ** 0.5) + 1):
            if num % i == 0:
                return False
        return True

    def get_prime_factors(num: int) -> List[int]:
        """Get prime factors of a number."""
        factors = []
        for i in range(2, num + 1):
            if num % i == 0 and is_prime(i):
                factors.append(i)
                num //= i
                while num % i == 0:
                    factors.append(i)
                    num //= i
        return factors

    return get_prime_factors(n)


# Test the function
print(factorize(8))   # [2, 2, 2]
print(factorize(25))  # [5, 5]
print(factorize(70))  # [2, 5, 7]
```