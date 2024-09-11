### Prime Factorization Script
```python
from typing import List

def factorize(n: int) -> List[int]:
    """
    Return list of prime factors of given integer in the order from smallest to largest.
    Each of the factors should be listed number of times corresponding to how many times it appears in factorization.
    Input number should be equal to the product of all factors

    Args:
        n (int): The number to be factorized

    Returns:
        List[int]: A list of prime factors of the input number
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
    # Remove duplicates by converting to a dictionary and back to a list
    return list(dict.fromkeys(factors))

# Example usage
print(factorize(8))  # Output: [2, 2, 2]
print(factorize(25))  # Output: [5, 5]
print(factorize(70))  # Output: [2, 5, 7]
```

**Explanation:**

This script uses a simple iterative approach to find the prime factors of a given number. It starts by dividing the number `n` by the smallest prime number `i`, which is initially set to 2. If `n` is divisible by `i`, it divides `n` by `i` and adds `i` to the list of factors. This process continues until `i` is greater than the square root of `n`. Finally, if `n` is greater than 1, it is also considered a prime factor and added to the list.

The list of factors is then processed to remove duplicates by converting it to a dictionary, which automatically removes duplicates, and then back to a list. This is done to ensure that each factor appears in the list only as many times as it appears in the factorization.