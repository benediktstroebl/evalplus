```python
from typing import List

def factorize(n: int) -> List[int]:
    """
    Return list of prime factors of given integer in the order from smallest to largest.
    Each of the factors should be listed number of times corresponding to how many times it appeares in factorization.
    Input number should be equal to the product of all factors
    
    :param n: Input number
    :return: List of prime factors
    """
    def recursive_factorize(n: int, i: int, factors: List[int]) -> List[int]:
        """
        Recursive helper function for factorize
        
        :param n: Input number
        :param i: Current divisor
        :param factors: List of prime factors found so far
        :return: List of prime factors
        """
        # Base case: if n is 1, we have found all factors
        if n == 1:
            return factors
        
        # If i is a divisor of n, divide n by i and add i to factors
        if n % i == 0:
            return recursive_factorize(n // i, i, factors + [i])
        
        # If i is not a divisor of n, try the next number
        return recursive_factorize(n, i + 1, factors)

    return recursive_factorize(n, 2, [])

# Test cases
print(factorize(8))   # [2, 2, 2]
print(factorize(25))  # [5, 5]
print(factorize(70))  # [2, 5, 7]
```