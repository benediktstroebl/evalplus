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
    print(factorize(8))   # Output: [2, 2, 2]
    print(factorize(25))  # Output: [5, 5]
    print(factorize(70))  # Output: [2, 5, 7]
```

This script defines a function `factorize` that takes an integer `n` and returns a list of its prime factors. It uses a while loop to iterate over possible factors, starting from 2 and increasing by 1 until the square root of `n`. If `n` is divisible by the current factor `i`, it divides `n` by `i` and adds `i` to the list of factors. Finally, if `n` is greater than 1 after the loop, it is a prime factor and is added to the list. The function returns the list of factors. The example usage demonstrates the function with three test cases.