```python
from typing import List

def factorize(n: int) -> List[int]:
    """
    Return list of prime factors of given integer in the order from smallest to largest.
    Each of the factors should be listed number of times corresponding to how many times it appeares in factorization.
    Input number should be equal to the product of all factors
    
    :param n: The number to be factorized
    :return: A list of prime factors
    """
    def is_prime(num: int) -> bool:
        """
        Helper function to check if a number is prime.
        
        :param num: The number to check
        :return: True if the number is prime, False otherwise
        """
        if num < 2:
            return False
        for i in range(2, int(num**0.5) + 1):
            if num % i == 0:
                return False
        return True

    factors = []
    for i in range(2, n + 1):
        if n % i == 0 and is_prime(i):
            while n % i == 0:
                factors.append(i)
                n //= i
    return factors

# Test the function
print(factorize(8))   # [2, 2, 2]
print(factorize(25))  # [5, 5]
print(factorize(70))  # [2, 5, 7]
```

This script defines a function `factorize` that takes an integer `n` as input and returns a list of prime factors. The function uses a helper function `is_prime` to check if a number is prime. It iterates over the numbers from 2 to `n`, checks if the number is prime and if `n` is divisible by the number, and if so, divides `n` by the number and adds it to the list of factors. The function returns the list of factors.

The script also includes test cases to verify the correctness of the function.