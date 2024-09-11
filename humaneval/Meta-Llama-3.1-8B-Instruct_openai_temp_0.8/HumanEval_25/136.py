```python
from typing import List


def factorize(n: int) -> List[int]:
    """
    Return list of prime factors of given integer in the order from smallest to largest.
    Each of the factors should be listed number of times corresponding to how many times it appeares in factorization.
    Input number should be equal to the product of all factors

    Args:
        n (int): The number to factorize.

    Returns:
        List[int]: A list of prime factors.
    """
    factors = []
    i = 2

    # Keep dividing the number by 2 while it's divisible
    while n % 2 == 0:
        factors.append(2)
        n = n // 2

    # Now i is 2, check every number from 3 to sqrt(n) to see if they're factors
    for i in range(3, int(n**0.5) + 1, 2):
        while n % i == 0:
            factors.append(i)
            n = n // i

    # If n is greater than 2, then it must be a prime number
    if n > 2:
        factors.append(n)

    return factors


# Test cases
print(factorize(8))  # [2, 2, 2]
print(factorize(25))  # [5, 5]
print(factorize(70))  # [2, 5, 7]
```

This script uses a simple loop to find all the prime factors of the given integer. It starts by dividing the number by 2 as long as it's divisible, then it checks every odd number from 3 to the square root of the number to see if they're factors, and finally if the remaining number is greater than 2, it must be a prime number.