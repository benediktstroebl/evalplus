### Factorize Function
#### A Python Function to Find Prime Factors of a Given Integer

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
    n (int): The input integer to be factorized

    Returns:
    List[int]: A list of prime factors of the input integer

    Examples:
    >>> factorize(8)
    [2, 2, 2]
    >>> factorize(25)
    [5, 5]
    >>> factorize(70)
    [2, 5, 7]
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

### Example Usage
print(factorize(8))   # [2, 2, 2]
print(factorize(25))  # [5, 5]
print(factorize(70))  # [2, 5, 7]
```

### How It Works
1. We start by initializing an empty list `factors` to store the prime factors and a variable `i` to 2 (the smallest prime number).
2. We then enter a while loop that continues until `i` squared is less than or equal to the input number `n`.
3. Inside the loop, we first check if `n` is divisible by `i`. If it is not, we increment `i` by 1 and repeat the check.
4. If `n` is divisible by `i`, we divide `n` by `i` and append `i` to the `factors` list. This process continues until `n` is no longer divisible by `i`.
5. Once `i` squared is greater than `n`, we check if `n` is greater than 1. If it is, we append `n` to the `factors` list, as `n` must be a prime number greater than `i`.
6. Finally, we return the `factors` list, which contains the prime factors of the input number `n` in the order from smallest to largest.