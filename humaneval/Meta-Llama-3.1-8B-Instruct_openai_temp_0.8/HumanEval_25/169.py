### Prime Factorization of an Integer
#### Script Description
This Python script uses a function `factorize()` to find the prime factors of a given integer. The function returns a list of prime factors, with each factor repeated according to its frequency in the factorization.

#### Code
```python
from typing import List

def factorize(n: int) -> List[int]:
    """
    Return list of prime factors of given integer in the order from smallest to largest.
    Each of the factors should be listed number of times corresponding to how many times it appears in factorization.
    Input number should be equal to the product of all factors

    Args:
        n (int): The input number to be factorized

    Returns:
        List[int]: A list of prime factors of the input number

    Examples:
        >>> factorize(8)
        [2, 2, 2]
        >>> factorize(25)
        [5, 5]
        >>> factorize(70)
        [2, 2, 5, 7]
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

# Example usage
print(factorize(8))   # Output: [2, 2, 2]
print(factorize(25))  # Output: [5, 5]
print(factorize(70))  # Output: [2, 2, 5, 7]
```

#### How it Works

The script uses a simple trial division method to find the prime factors of the input number `n`.

1.  Initialize an empty list `factors` to store the prime factors.
2.  Start with `i = 2` (the smallest prime number).
3.  As long as `i * i <= n`, check if `n` is divisible by `i`. If it is, then `i` is a prime factor, and we divide `n` by `i` and append `i` to the `factors` list.
4.  If `n` is not divisible by `i`, increment `i` by 1.
5.  Once `i * i > n`, it means `n` is a prime number itself, so we append it to the `factors` list.
6.  Finally, return the `factors` list, which contains the prime factors of the input number `n`.

The script uses a simple and efficient approach to find the prime factors of an integer. It has a time complexity of O(sqrt(n)), making it suitable for large input numbers.