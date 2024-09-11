```python
from typing import List

def factorize(n: int) -> List[int]:
    """
    Return list of prime factors of given integer in the order from smallest to largest.
    Each of the factors should be listed number of times corresponding to how many times it appeares in factorization.
    Input number should be equal to the product of all factors

    :param n: Input integer
    :return: List of prime factors
    """
    def prime_factors(n: int) -> List[int]:
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

    return prime_factors(n)

# Test cases
print(factorize(8))   # [2, 2, 2]
print(factorize(25))  # [5, 5]
print(factorize(70))  # [2, 5, 7]
```

In this script, we define a helper function `prime_factors` inside the `factorize` function. This function generates prime factors of the input number `n` by dividing it by the smallest divisor `i` until `n` is no longer divisible by `i`. The process continues until `n` is reduced to 1. The prime factors are stored in the `factors` list, which is then returned.

Note: The test cases are included to verify the correctness of the function.