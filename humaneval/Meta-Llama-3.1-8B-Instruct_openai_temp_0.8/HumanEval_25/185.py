### Factorize Function
```python
from typing import List

def factorize(n: int) -> List[int]:
    """
    Return list of prime factors of given integer in the order from smallest to largest.
    Each of the factors should be listed number of times corresponding to how many times it appears in factorization.
    Input number should be equal to the product of all factors

    Args:
        n (int): The number to factorize

    Returns:
        List[int]: A list of prime factors of n
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
if __name__ == "__main__":
    print(factorize(8))  # [2, 2, 2]
    print(factorize(25))  # [5, 5]
    print(factorize(70))  # [2, 5, 7]
```

In this code, the `factorize` function takes an integer `n` as input and returns a list of its prime factors. The function works by continuously dividing `n` by the smallest prime factor until `n` is reduced to 1. The prime factors are added to the `factors` list each time a division is performed. This process ensures that the prime factors are listed in increasing order. If `n` itself is a prime number greater than 1, it is added to the list at the end.