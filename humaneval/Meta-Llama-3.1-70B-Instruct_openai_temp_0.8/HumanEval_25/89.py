```python
from typing import List

def factorize(n: int) -> List[int]:
    """
    Return list of prime factors of given integer in the order from smallest to largest.
    Each of the factors should be listed number of times corresponding to how many times it appears in factorization.
    Input number should be equal to the product of all factors

    :param n: Input number to be factorized
    :return: List of prime factors
    """
    def is_prime(num: int) -> bool:
        """
        Helper function to check if a number is prime
        """
        if num < 2:
            return False
        for i in range(2, int(num**0.5) + 1):
            if num % i == 0:
                return False
        return True

    factors = []
    divisor = 2
    while n > 1:
        # Find the smallest divisor of n
        while n % divisor!= 0:
            divisor += 1
            # Check if divisor is prime
            if not is_prime(divisor):
                divisor += 1
        # Keep dividing n by the divisor until it's no longer divisible
        while n % divisor == 0:
            factors.append(divisor)
            n = n // divisor
        # Increment divisor to find the next prime factor
        divisor += 1
    return factors

# Test cases
print(factorize(8))   # [2, 2, 2]
print(factorize(25))  # [5, 5]
print(factorize(70))  # [2, 5, 7]
```

Explanation:

1. We define a helper function `is_prime(num)` to check if a number is prime.
2. The main function `factorize(n)` finds the smallest divisor of `n` and keeps dividing `n` by this divisor until it's no longer divisible.
3. We increment the divisor to find the next prime factor.
4. The process is repeated until `n` is reduced to 1.
5. The list of prime factors is returned in the order from smallest to largest, with each factor listed the number of times it appears in the factorization.