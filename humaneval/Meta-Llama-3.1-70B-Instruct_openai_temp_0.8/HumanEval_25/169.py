```python
from typing import List

def factorize(n: int) -> List[int]:
    """
    Return list of prime factors of given integer in the order from smallest to largest.
    Each of the factors should be listed number of times corresponding to how many times it appears in factorization.
    Input number should be equal to the product of all factors
    
    :param n: The number to be factorized.
    :return: A list of prime factors.
    """
    factors = []
    i = 2
    while i * i <= n:
        if n % i:
            i += 1
        else:
            n //= i
            factors.append(i)
    if n > 1:
        factors.append(n)
    return factors

# Test cases
print(factorize(8))  # [2, 2, 2]
print(factorize(25))  # [5, 5]
print(factorize(70))  # [2, 5, 7]
```

This script defines a function `factorize` that takes an integer `n` as input and returns a list of its prime factors. The function uses a simple trial division method to find the prime factors. It starts by dividing the input number `n` by the smallest prime number, which is 2, and then continues dividing by the smallest prime number until it can no longer divide. The quotient is then divided by the next smallest prime number, and so on. The process continues until the quotient is reduced to 1.

The test cases are included at the end of the script to verify the correctness of the `factorize` function.