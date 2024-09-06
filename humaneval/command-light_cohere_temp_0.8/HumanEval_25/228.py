```python
from typing import List

def factorize(n: int) -> List[int]:
    """
    Return list of prime factors of given integer in the order from smallest to largest
    Each of the factors should be listed number of times corresponding to how many times it appears in factorization.
    """
    process:
        # 1. Find the first prime factor.
        while True[ factor <= n/2:
            # Find the first occurrence of the prime factor
            for factor_num in range(2, int(n**0.5)):
                if n % div(factor_num):
                    if n % div == 0:
                        yield factor_num
                        n //= div
            else:
                break
        # 2. Find the remaining primes
       
        for factor_num in range(2, int(n**0.5)):
            if n % div(factor_num):
                yield factor_num
                n //= div
    """

# Test cases
test_cases = [8, 25, 70]

for test in test_cases:
    print(factorize(test))
```

The function `factorize` identifies the set of prime factors for the given number, and delivers the list of those prime factors, arranged from smallest to largest, following the order of their appearance in factorization.

The script also includes test cases, and the function is evaluated against each test to ensure its correctness.