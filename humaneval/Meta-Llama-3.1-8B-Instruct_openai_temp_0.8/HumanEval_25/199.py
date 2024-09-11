```python
from typing import List
import math

def factorize(n: int) -> List[int]:
    """
    Return list of prime factors of given integer in the order from smallest to largest.
    Each of the factors should be listed number of times corresponding to how many times it appears in factorization.
    Input number should be equal to the product of all factors

    Args:
    n (int): The number to be factorized

    Returns:
    List[int]: A list of prime factors
    """
    factors = []
    i = 2
    while n > 1:
        # Check if i is a factor of n
        if n % i == 0:
            # If i is a factor, add it to the factors list
            factors.append(i)
            n = n // i
        else:
            # If i is not a factor, increment i by 1
            i += 1
            # Check if i is a prime number
            while not is_prime(i):
                i += 1
    return factors

def is_prime(n: int) -> bool:
    """
    Check if a number is prime

    Args:
    n (int): The number to be checked

    Returns:
    bool: True if the number is prime, False otherwise
    """
    if n <= 1:
        return False
    if n == 2:
        return True
    if n % 2 == 0:
        return False
    max_divisor = math.floor(math.sqrt(n))
    for d in range(3, 1 + max_divisor, 2):
        if n % d == 0:
            return False
    return True

if __name__ == "__main__":
    print(factorize(8))  
    print(factorize(25))
    print(factorize(70))
```

This script uses a helper function `is_prime` to check if a number is prime. The `factorize` function uses this helper function to find the prime factors of a given number. It does this by dividing the number by the smallest possible divisor (2) until it is no longer divisible, then incrementing the divisor and checking if the number is prime. This process is repeated until the number is reduced to 1.