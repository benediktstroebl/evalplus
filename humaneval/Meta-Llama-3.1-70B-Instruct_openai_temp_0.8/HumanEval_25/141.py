```python
from typing import List
import math

def factorize(n: int) -> List[int]:
    """
    Return list of prime factors of given integer in the order from smallest to largest.
    Each of the factors should be listed number of times corresponding to how many times it appears in factorization.
    
    :param n: Input number
    :return: List of prime factors
    """
    factors = []
    # Start from 2, the smallest prime number
    i = 2
    while i * i <= n:
        # If n is divisible by i, it is a factor
        if n % i:
            # If not, increment i by 1
            i += 1
        else:
            # If it is a factor, add it to the list and divide n by i
            n //= i
            factors.append(i)
    # If n is a prime number greater than 1, it is a factor
    if n > 1:
        factors.append(n)
    return factors


# Test the function
print(factorize(8))   # [2, 2, 2]
print(factorize(25))  # [5, 5]
print(factorize(70))  # [2, 5, 7]

def test_factorize():
    # Test cases
    assert math.prod(factorize(8)) == 8
    assert math.prod(factorize(25)) == 25
    assert math.prod(factorize(70)) == 70
    print("All tests passed.")

test_factorize()
```

The `factorize` function works by dividing the input number `n` by the smallest prime number (2) as long as it's divisible. Then it increments the divisor by 1 and continues this process until `n` is no longer divisible by the current divisor. This process continues until `n` is reduced to 1. The list of divisors that were used to reduce `n` to 1 are the prime factors of `n`. 

The test cases verify that the product of the prime factors is equal to the original number.