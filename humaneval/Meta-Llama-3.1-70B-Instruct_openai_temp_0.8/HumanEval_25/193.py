```python
from typing import List

def factorize(n: int) -> List[int]:
    """
    Return list of prime factors of given integer in the order from smallest to largest.
    Each of the factors should be listed number of times corresponding to how many times it appeares in factorization.
    Input number should be equal to the product of all factors
    
    Args:
        n (int): The number to be factorized.
    
    Returns:
        List[int]: A list of prime factors.
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

This script defines the `factorize` function which finds the prime factors of a given number `n`. It starts by dividing `n` by the smallest prime number, which is 2. If `n` is divisible by the current number `i`, it appends `i` to the `factors` list and divides `n` by `i`. If `n` is not divisible by `i`, it increments `i` by 1. This process continues until `i` is greater than the square root of `n`. If `n` is greater than 1 at the end of the loop, it means `n` is a prime number and it is appended to the `factors` list. The function then returns the `factors` list.