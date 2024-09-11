```python
from typing import List

def factorize(n: int) -> List[int]:
    """
    Return list of prime factors of given integer in the order from smallest to largest.
    Each of the factors should be listed number of times corresponding to how many times it appeares in factorization.
    
    Args:
    n (int): The number to be factorized.
    
    Returns:
    List[int]: A list of prime factors.
    """
    
    def is_prime(num: int) -> bool:
        """
        Helper function to check if a number is prime.
        
        Args:
        num (int): The number to be checked.
        
        Returns:
        bool: True if the number is prime, False otherwise.
        """
        if num < 2:
            return False
        for i in range(2, int(num**0.5) + 1):
            if num % i == 0:
                return False
        return True

    factors = []
    for i in range(2, n + 1):
        # Only consider prime numbers
        if is_prime(i):
            # Keep dividing the number by the current prime factor until it's no longer divisible
            while n % i == 0:
                factors.append(i)
                n //= i
    return factors

# Test cases
print(factorize(8))   # [2, 2, 2]
print(factorize(25))  # [5, 5]
print(factorize(70))  # [2, 5, 7]
```

In the script above, the `factorize` function calculates the prime factors of a given integer. It does this by checking each number from 2 up to the given number to see if it's a prime number and if the given number is divisible by it. If the number is divisible, it's divided by the current prime factor and this process continues until the number is no longer divisible. The prime factors are appended to a list which is then returned.

The `is_prime` function is a helper function used to check if a number is prime. It does this by checking if the number is divisible by any number from 2 up to the square root of the number. If it is, it's not a prime number. If it's not divisible by any of these numbers, it is a prime number.

The test cases at the end of the script demonstrate the function's usage and verify that it's working correctly.