### Prime Factorization of an Integer
#### Problem Statement
Return list of prime factors of given integer in the order from smallest to largest. Each of the factors should be listed number of times corresponding to how many times it appears in factorization.

#### Solution
```python
from typing import List

def factorize(n: int) -> List[int]:
    """
    Return list of prime factors of given integer in the order from smallest to largest.
    
    Args:
    n (int): The input number to factorize.
    
    Returns:
    List[int]: A list of prime factors of the input number.
    """
    def is_prime(num: int) -> bool:
        """Check if a number is prime."""
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

# Example use cases
if __name__ == "__main__":
    print(factorize(8))  # [2, 2, 2]
    print(factorize(25))  # [5, 5]
    print(factorize(70))  # [2, 5, 7]
```

This script defines a function `factorize(n)` that takes an integer `n` as input and returns a list of its prime factors. The function uses a helper function `is_prime(num)` to check if a number is prime. The main function iterates through numbers from 2 to the square root of `n` to find prime factors and divides `n` by the found factor until it is no longer divisible. If a number is not divisible by any number up to its square root, it is a prime number and is added to the list of factors. The function finally checks if the remaining `n` is a prime number greater than 1 and adds it to the list of factors if so.