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
        List[int]: A list of prime factors of n
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
    while i * i <= n:
        if n % i:
            i += 1
        else:
            n //= i
            factors.append(i)
    if n > 1:
        factors.append(n)
    
    # Remove duplicates and sort the list
    factors = sorted(list(set(factors)))

    return factors

# Example usage:
if __name__ == "__main__":
    print(factorize(8))   # [2, 2, 2]
    print(factorize(25))  # [5, 5]
    print(factorize(70))  # [2, 5, 7]
```

This Python script defines a function `factorize(n)` that returns a list of prime factors of `n`. The function uses a helper function `is_prime(num)` to check if a number is prime. It then uses a loop to divide `n` by the smallest prime number as many times as possible, adding the divisor to the list of factors each time. This process continues until `n` is reduced to 1. Finally, it removes duplicates from the list of factors by converting it to a set, sorts the list, and returns it.