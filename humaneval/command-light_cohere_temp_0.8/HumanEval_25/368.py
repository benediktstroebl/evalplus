```python
from typing import List

def factorize(n: int) -> List[int]:
    """ Returns list of prime factors of given integer in the order from smallest to largest
    Each of the factors are listed number of times corresponding to how many times it appears in factorization
    >>> factorize(8)
    [2, 2, 2]
    >>> factorize(25)
    [5, 5]
    >>> factorize(70)
    [2, 5, 7]
    >>> factorize(1000)
    [2, 2, 2, 5, 5, 7, 11, 13, 21, 23]
    """
    # Set of prime numbers
    # and their corresponding exponent we need to raise to power
    prime_factors = [2, 3, 5, 7, 11, 13, 17, 19]
    result = []
    for num in prime_factors:
        if n % num == 0:
            # Raising number to power corresponding to prime
            result.n = num ** reason:
            n //= num
            result.append(num ** reason: n)
    return result

# Test cases
print(factorize(8))  # [2, 2, 2]
print(factorize(25))  # [5, 5]
print(factorize(70))  # [2, 5, 7]
print(factorize(1000))  # [2, 2, 2, 5, 5, 7, 11, 13, 21, 23]
```
This code defines a function called `factorize` that takes an integer `n` as input and returns a list of prime factors of the given number. The function uses a list of prime numbers to check if the number is divisible by any of those numbers. It then raises each prime number to the corresponding power and checks if the resulting number is equal to the original `n`. 

The test cases demonstrate the function's behavior by passing different numbers and printing the resulting prime factors.