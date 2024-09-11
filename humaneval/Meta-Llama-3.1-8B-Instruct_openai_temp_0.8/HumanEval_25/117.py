### Factorization of an Integer
#### Problem Statement
Given an integer `n`, return a list of its prime factors in the order from smallest to largest, where each factor is listed the number of times it appears in the factorization.

#### Solution
```python
from typing import List

def factorize(n: int) -> List[int]:
    """
    Return list of prime factors of given integer in the order from smallest to largest.
    Each of the factors should be listed number of times corresponding to how many times it appears in factorization.
    Input number should be equal to the product of all factors

    Args:
        n (int): The input integer to factorize.

    Returns:
        List[int]: A list of prime factors of the input integer.
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

# Example use cases
if __name__ == "__main__":
    print(factorize(8))  # [2, 2, 2]
    print(factorize(25))  # [5, 5]
    print(factorize(70))  # [2, 5, 7]
```

#### Explanation
This script defines a function `factorize(n)` that takes an integer `n` as input and returns a list of its prime factors.
The function uses a simple trial division method to find the prime factors:
1.  It starts from `i = 2`, which is the smallest prime number.
2.  It checks if `n` is divisible by `i` by using the modulo operator (`n % i`).
3.  If `n` is divisible by `i`, it divides `n` by `i` and appends `i` to the list of factors.
4.  It repeats this process until `i` is greater than the square root of `n`.
5.  If `n` is not divisible by any of the numbers from `2` to `sqrt(n)`, it means that `n` itself is a prime number, so it appends `n` to the list of factors.
6.  Finally, it returns the list of factors.

The example use cases demonstrate the usage of the `factorize(n)` function with different inputs.