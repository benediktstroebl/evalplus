```python
from typing import List

def factorize(n: int) -> List[int]:
    """
    Return list of prime factors of given integer in the order from smallest to largest.
    Each of the factors should be listed number of times corresponding to how many times it appears in factorization.
    Input number should be equal to the product of all factors
    """
    def get_prime_factors(n: int) -> List[int]:
        i = 2
        factors = []
        while i * i <= n:
            if n % i:
                i += 1
            else:
                n //= i
                factors.append(i)
        if n > 1:
            factors.append(n)
        return factors

    prime_factors = get_prime_factors(n)
    return prime_factors

# Test the function
assert factorize(8) == [2, 2, 2]
assert factorize(25) == [5, 5]
assert factorize(70) == [2, 5, 7]
```

This script works by checking all numbers from 2 up to the square root of the input number `n`, and if `n` is divisible by that number, dividing `n` by that number and adding it to the list of factors. This process is repeated until `n` is reduced to 1. If `n` is a prime number greater than 1 at the end of the process, it is also added to the list of factors. The result is a list of prime factors in the order from smallest to largest, with each factor listed as many times as it appears in the factorization of the input number.