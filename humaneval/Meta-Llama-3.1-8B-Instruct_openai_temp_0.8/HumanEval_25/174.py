### Prime Factorization of a Number
#### Script
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
        List[int]: A list of prime factors
    """
    factors = []
    i = 2

    # Divide the number by the smallest possible factor (2) as long as it's divisible
    while n % i == 0:
        factors.append(i)
        n = n // i

    # Now we have n as a prime number (if it was not a multiple of 2)
    # So we start with the next possible factor, which is the square root of n
    i = 3
    while i * i <= n:
        # If n is divisible by i, it means i is a factor
        if n % i == 0:
            factors.append(i)
            n = n // i
        # If n is not divisible by i, we try the next number
        else:
            i += 2

    # If n is a prime number greater than 2 (which we haven't checked yet)
    if n > 2:
        factors.append(n)

    return factors

# Test the function
print(factorize(8))    # [2, 2, 2]
print(factorize(25))   # [5, 5]
print(factorize(70))   # [2, 5, 7]
```

#### Explanation

This script defines a function `factorize` that takes an integer `n` as input and returns a list of its prime factors.

The function starts by dividing `n` by the smallest possible factor, which is 2, as long as it's divisible. This is done by a while loop that continues as long as `n` is divisible by `i`.

Once `n` is no longer divisible by 2, we start with the next possible factor, which is the square root of `n`. We do this by initializing `i` to 3 and checking if `n` is divisible by `i`. If it is, we append `i` to the list of factors and divide `n` by `i`. If it's not, we increment `i` by 2.

This process continues until `n` is reduced to 1. If `n` is a prime number greater than 2, it will be appended to the list of factors at the end.

Finally, the script tests the function with some examples.