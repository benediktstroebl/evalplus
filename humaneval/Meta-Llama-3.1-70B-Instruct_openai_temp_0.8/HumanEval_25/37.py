```python
from typing import List

def factorize(n: int) -> List[int]:
    """
    Return list of prime factors of given integer in the order from smallest to largest.
    Each of the factors should be listed number of times corresponding to how many times it appeares in factorization.
    Input number should be equal to the product of all factors

    Args:
        n (int): Input number to be factorized

    Returns:
        List[int]: A list of prime factors in the order from smallest to largest
    """
    def is_prime(num: int) -> bool:
        """Check if a number is prime"""
        if num < 2:
            return False
        for i in range(2, int(num**0.5) + 1):
            if num % i == 0:
                return False
        return True

    factors = []
    divisor = 2
    while n > 1:
        while n % divisor == 0:
            factors.append(divisor)
            n //= divisor
        divisor += 1
        # If divisor is not prime, it can't divide the number, so we can skip it
        while not is_prime(divisor):
            divisor += 1
    return factors


# Test cases
print(factorize(8))   # [2, 2, 2]
print(factorize(25))  # [5, 5]
print(factorize(70))  # [2, 5, 7]
```

The `factorize` function works by dividing the input number `n` by the smallest divisor (starting from 2) until it is no longer divisible. It then increments the divisor and repeats the process until `n` is reduced to 1. The prime factors are appended to the `factors` list in the order they are found.

The `is_prime` function checks whether a number is prime by checking divisibility up to the square root of the number. This is an optimization to reduce the number of checks required.

Note that the `is_prime` function is not necessary for this particular problem, as we are already checking divisibility in the `factorize` function. However, it is included to make the code more efficient and to demonstrate a common technique for optimizing primality checks.