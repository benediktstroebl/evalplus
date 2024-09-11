```python
from typing import List


def factorize(n: int) -> List[int]:
    """
    Return list of prime factors of given integer in the order from smallest to largest.
    Each of the factors should be listed number of times corresponding to how many times it appears in factorization.
    Input number should be equal to the product of all factors

    Args:
        n (int): The number to factorize

    Returns:
        List[int]: A list of prime factors
    """

    def is_prime(num: int) -> bool:
        """ Checks if a number is prime """
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
            if is_prime(i):
                factors.append(i)
    if n > 1 and is_prime(n):
        factors.append(n)
    return factors


# Example usage:
if __name__ == "__main__":
    print(factorize(8))  # Output: [2, 2, 2]
    print(factorize(25))  # Output: [5, 5]
    print(factorize(70))  # Output: [2, 5, 7]
```

This script defines a function `factorize(n)` that takes an integer `n` and returns a list of its prime factors. The function uses a helper function `is_prime(num)` to check if a number is prime. The main function iterates from 2 to the square root of `n`, checking if each number is a factor of `n`. If it is, the number is divided by the factor, and if the factor is prime, it is added to the list of factors. The process continues until `n` is reduced to 1. Finally, if `n` is greater than 1 and prime, it is added to the list of factors.