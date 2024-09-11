```python
from typing import List

def factorize(n: int) -> List[int]:
    """
    Return list of prime factors of given integer in the order from smallest to largest.
    Each of the factors should be listed number of times corresponding to how many times it appears in factorization.
    Input number should be equal to the product of all factors

    Args:
        n (int): The number to be factorized

    Returns:
        List[int]: A list of prime factors of the given number
    """
    def is_prime(num: int) -> bool:
        """Check if a number is prime"""
        if num < 2:
            return False
        for i in range(2, int(num ** 0.5) + 1):
            if num % i == 0:
                return False
        return True

    factors = []
    i = 2
    while n > 1:
        if n % i == 0:
            n //= i
            if is_prime(i):
                factors.append(i)
        else:
            i += 1
    return factors


# Example usage
print(factorize(8))  # Output: [2, 2, 2]
print(factorize(25))  # Output: [5, 5]
print(factorize(70))  # Output: [2, 5, 7]
```

This script defines a function `factorize` that calculates the prime factors of a given integer. It uses a helper function `is_prime` to check if a number is prime. The main function iterates from 2 to the square root of the input number, and for each factor found, it updates the input number by dividing it by the factor, and checks if the factor is prime. If it is, the factor is added to the list of factors.