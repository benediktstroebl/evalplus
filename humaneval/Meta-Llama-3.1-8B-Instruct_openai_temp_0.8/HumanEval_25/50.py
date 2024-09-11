```python
from typing import List

def factorize(n: int) -> List[int]:
    """
    Return list of prime factors of given integer in the order from smallest to largest.
    Each of the factors should be listed number of times corresponding to how many times it appears in factorization.
    Input number should be equal to the product of all factors
    
    Parameters:
    n (int): The number to be factorized
    
    Returns:
    List[int]: A list of prime factors
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
        # Check if i is a factor of n
        if n % i == 0:
            # Check if i is prime
            if is_prime(i):
                factors.append(i)
            # Divide n by i
            n = n // i
        else:
            # If i is not a factor of n, increment i
            i += 1
    return factors

# Example usage
print(factorize(8))  # [2, 2, 2]
print(factorize(25))  # [5, 5]
print(factorize(70))  # [2, 5, 7]
```

This script uses a helper function `is_prime` to check if a number is prime. The main function `factorize` iterates from 2 to `n` (inclusive), and for each number `i`, it checks if `i` is a factor of `n`. If `i` is a factor, it checks if `i` is prime and appends it to the list of factors. Then, it divides `n` by `i`. If `i` is not a factor of `n`, it increments `i`. The loop continues until `n` is reduced to 1.