```python
from typing import List

def factorize(n: int) -> List[int]:
    """
    Return list of prime factors of given integer in the order from smallest to largest.
    Each of the factors should be listed number of times corresponding to how many times it appeares in factorization.
    Input number should be equal to the product of all factors
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

    def get_next_prime(num: int) -> int:
        """
        Helper function to get the next prime number
        """
        num += 1
        while not is_prime(num):
            num += 1
        return num

    factors = []
    i = 2
    while i * i <= n:
        if n % i:
            i = get_next_prime(i)
        else:
            n //= i
            factors.append(i)
    if n > 1:
        factors.append(n)
    return factors

# Example usage:
print(factorize(8))    # [2, 2, 2]
print(factorize(25))   # [5, 5]
print(factorize(70))   # [2, 5, 7]
```