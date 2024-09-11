```python
from typing import List

def factorize(n: int) -> List[int]:
    """
    Return list of prime factors of given integer in the order from smallest to largest.
    Each of the factors should be listed number of times corresponding to how many times it appears in factorization.
    Input number should be equal to the product of all factors
    
    :param n: Input integer
    :return: List of prime factors
    """
    def is_prime(num: int) -> bool:
        """
        Check if a number is prime
        
        :param num: Input number
        :return: True if number is prime, False otherwise
        """
        if num < 2:
            return False
        for i in range(2, int(num ** 0.5) + 1):
            if num % i == 0:
                return False
        return True

    def get_prime_factors(num: int) -> List[int]:
        """
        Get prime factors of a number
        
        :param num: Input number
        :return: List of prime factors
        """
        factors = []
        for i in range(2, num + 1):
            if is_prime(i):
                while num % i == 0:
                    factors.append(i)
                    num //= i
        return factors

    return get_prime_factors(n)

# Test cases
print(factorize(8))  # [2, 2, 2]
print(factorize(25))  # [5, 5]
print(factorize(70))  # [2, 5, 7]
```