```python
from typing import List

def factorize(n: int) -> List[int]:
    """
    Return list of prime factors of given integer in the order from smallest to largest.
    Each of the factors should be listed number of times corresponding to how many times it appears in factorization.
    Input number should be equal to the product of all factors

    Args:
        n (int): The number to be factorized.

    Returns:
        List[int]: A list of prime factors of the given number.
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
        # Check if i is a divisor
        if n % i:
            # If not, increment i by 1
            i += 1
        else:
            # If i is a divisor, append it to factors and divide n by i
            count = 0
            while n % i == 0:
                count += 1
                n //= i
            factors.extend([i] * count)
    # If n is not 1, that means it is a prime number
    if n > 1:
        factors.append(n)
    return factors


# Example use cases:
if __name__ == "__main__":
    print(factorize(8))  # Output: [2, 2, 2]
    print(factorize(25))  # Output: [5, 5]
    print(factorize(70))  # Output: [2, 5, 7]
```

This script uses a helper function `is_prime` to check if a number is prime. The main function `factorize` iterates over numbers from 2 to the square root of the input number and checks if they are factors. If a number is a factor, it appends it to the `factors` list and divides the input number by it. This process continues until the input number is reduced to 1, at which point the list of factors is returned.