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
        List[int]: A list of prime factors of the input number.
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

# Test cases
print(factorize(8))  # [2, 2, 2]
print(factorize(25))  # [5, 5]
print(factorize(70))  # [2, 5, 7]
```

This Python script defines a function `factorize(n)` that takes an integer `n` as input and returns a list of its prime factors, with each factor appearing in the list as many times as it appears in the factorization of `n`. The function uses a simple trial division method to find the prime factors. It iterates from 2 to the square root of `n` and checks if `n` is divisible by the current number. If it is, it divides `n` by the current number and adds it to the list of factors. If it's not, it increments the current number by 1. After the loop, if `n` is greater than 1, it means `n` itself is a prime factor, so it is added to the list of factors. The test cases at the end of the script demonstrate the function's correctness.