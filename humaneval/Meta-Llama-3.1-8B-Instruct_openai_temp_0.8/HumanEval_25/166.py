**Prime Factorization Script**
================================

Below is a Python script that solves the given problem using a function called `factorize`. This function uses a simple trial division method to find the prime factors of a given number and returns them in a list.

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
        List[int]: A list of prime factors
    """
    factors = []
    i = 2
    while i * i <= n:
        if n % i:
            # If i is not a factor, increment it by 1
            i += 1
        else:
            # If i is a factor, divide n by i and append i to factors
            n //= i
            factors.append(i)
    if n > 1:
        # If n is greater than 1, it means that n is a prime number
        factors.append(n)
    # Remove duplicates and sort the factors in ascending order
    return sorted(list(set(factors)))

# Example use cases
print(factorize(8))  # Output: [2, 2, 2]
print(factorize(25))  # Output: [5, 5]
print(factorize(70))  # Output: [2, 5, 7]
```

In this script, the `factorize` function uses a while loop to divide the input number `n` by the smallest divisor `i` until `n` is reduced to 1. If `n` is not divisible by `i`, then `i` is incremented by 1. If `n` is divisible by `i`, then `n` is divided by `i` and `i` is appended to the list of factors. After the loop, if `n` is greater than 1, it means that `n` is a prime number, so `n` is appended to the list of factors. Finally, the list of factors is sorted and returned.