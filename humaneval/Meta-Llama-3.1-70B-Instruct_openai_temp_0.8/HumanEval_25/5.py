```python
from typing import List

def factorize(n: int) -> List[int]:
    """
    Return list of prime factors of given integer in the order from smallest to largest.
    Each of the factors should be listed number of times corresponding to how many times it appeares in factorization.
    Input number should be equal to the product of all factors

    :param n: integer to be factorized
    :return: list of prime factors
    """
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


# Example usage:
print(factorize(8))     # [2, 2, 2]
print(factorize(25))    # [5, 5]
print(factorize(70))    # [2, 5, 7]
print(factorize(100))   # [2, 2, 5, 5]
```

This function works by dividing the input number `n` by the smallest prime factor (2) as long as it's divisible. Then it increments the divisor until it finds the next number that can divide `n`, which will necessarily be a prime factor. This process continues until `n` is reduced to 1. The list of divisors that were used to reduce `n` to 1 are the prime factors of the original number. 

This solution has a time complexity of O(sqrt(n)) because the while loop runs until `i` is larger than the square root of `n`. The space complexity is O(log(n)) because in the worst case, `n` is a power of 2 and the list of factors will contain log2(n) elements.