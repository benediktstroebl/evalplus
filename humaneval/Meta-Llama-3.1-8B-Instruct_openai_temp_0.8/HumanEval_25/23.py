### Prime Factorization of an Integer

Here's a Python function that uses a simple iterative approach to compute the prime factors of a given integer.

```markdown
### Code

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

# Example usage
print(factorize(8))  # [2, 2, 2]
print(factorize(25))  # [5, 5]
print(factorize(70))  # [2, 5, 7]
```
### Explanation

1.  We start by initializing an empty list `factors` to store the prime factors of the input number `n`.
2.  We loop through integers from 2 to the square root of `n` (`i * i <= n`).
3.  Inside the loop, we first check if `n` is divisible by `i` using the modulo operator (`n % i`). If it is, we divide `n` by `i` and append `i` to the `factors` list.
4.  If `n` is not divisible by `i`, we increment `i` by 1.
5.  Once the loop completes, we check if the remaining `n` is greater than 1. If it is, we append it to the `factors` list, as it's a prime factor.
6.  Finally, we return the `factors` list.

This code has a time complexity of O(sqrt(n)) due to the loop constraint `i * i <= n`.