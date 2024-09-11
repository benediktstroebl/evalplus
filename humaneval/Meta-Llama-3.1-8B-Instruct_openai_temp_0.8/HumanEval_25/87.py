Here's a Python script using a prime factorization function based on the algorithm described in the problem statement:

```markdown
### Factorize Function
#### A Python function to prime factorize an integer.

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
        List[int]: A list of prime factors.

    Examples:
        >>> factorize(8)
        [2, 2, 2]
        >>> factorize(25)
        [5, 5]
        >>> factorize(70)
        [2, 5, 7]
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


# Example usage:
if __name__ == "__main__":
    print(factorize(8))  # Output: [2, 2, 2]
    print(factorize(25))  # Output: [5, 5]
    print(factorize(70))  # Output: [2, 5, 7]
```

This script defines a function called `factorize` that takes an integer `n` as input and returns a list of its prime factors. The function uses a while loop to check each number up to the square root of `n` to see if it's a factor. If it is, the function divides `n` by this factor and adds it to the list of factors. If the number isn't divisible by the current number, the function increments it and checks the next number. This continues until `n` is reduced to 1, at which point all of its prime factors have been found.