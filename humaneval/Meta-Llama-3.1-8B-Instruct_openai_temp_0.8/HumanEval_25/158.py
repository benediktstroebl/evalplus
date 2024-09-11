```python
from typing import List

def factorize(n: int) -> List[int]:
    """
    Return list of prime factors of given integer in the order from smallest to largest.
    Each of the factors should be listed number of times corresponding to how many times it appeares in factorization.
    Input number should be equal to the product of all factors

    Args:
        n (int): The number to be factorized.

    Returns:
        List[int]: A list of prime factors in the order from smallest to largest.
    """
    def is_prime(i: int) -> bool:
        """Check if a number is prime."""
        if i < 2:
            return False
        for j in range(2, int(i**0.5) + 1):
            if i % j == 0:
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


# Example use cases:
if __name__ == "__main__":
    print(factorize(8))  # [2, 2, 2]
    print(factorize(25))  # [5, 5]
    print(factorize(70))  # [2, 5, 7]
```

This script defines a function `factorize(n)` that takes an integer `n` as input and returns a list of its prime factors in the order from smallest to largest. The function `is_prime(i)` is used to check if a number is prime. The loop `while i * i <= n` is used to iterate through all possible factors of `n`, starting from 2 and increasing by 1 each time. If `n` is divisible by `i`, it is divided by `i` and `i` is added to the list of factors. Finally, if `n` is greater than 1, it means that `n` itself is a prime factor and it is added to the list.