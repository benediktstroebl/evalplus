```python
from typing import List

def factorize(n: int) -> List[int]:
    """
    Return list of prime factors of given integer in the order from smallest to largest.
    Each of the factors should be listed number of times corresponding to how many times it appears in factorization.
    Input number should be equal to the product of all factors

    :param n: The input number to be factorized
    :return: A list of prime factors
    """
    def is_prime(num: int) -> bool:
        """Check if a number is prime."""
        if num < 2:
            return False
        for i in range(2, int(num ** 0.5) + 1):
            if num % i == 0:
                return False
        return True

    factors = []
    divisor = 2

    # Find all prime factors
    while n > 1:
        if n % divisor == 0:
            if is_prime(divisor):
                factors.append(divisor)
                n = n // divisor
            else:
                divisor += 1
        else:
            divisor += 1

    return factors


# Test the function
print(factorize(8))   # Output: [2, 2, 2]
print(factorize(25))  # Output: [5, 5]
print(factorize(70))  # Output: [2, 5, 7]
```

However, there's a more efficient way to factorize a number in Python without manually checking for prime numbers. Here's an optimized version:

```python
from typing import List

def factorize(n: int) -> List[int]:
    """
    Return list of prime factors of given integer in the order from smallest to largest.
    Each of the factors should be listed number of times corresponding to how many times it appears in factorization.
    Input number should be equal to the product of all factors

    :param n: The input number to be factorized
    :return: A list of prime factors
    """
    factors = []
    divisor = 2

    # Find all prime factors
    while n > 1:
        while n % divisor == 0:
            factors.append(divisor)
            n = n // divisor
        divisor += 1

    return factors


# Test the function
print(factorize(8))   # Output: [2, 2, 2]
print(factorize(25))  # Output: [5, 5]
print(factorize(70))  # Output: [2, 5, 7]
```

In this version, we increment the divisor only when it's no longer a factor of `n`. This way, we avoid unnecessary checks and make the function more efficient.