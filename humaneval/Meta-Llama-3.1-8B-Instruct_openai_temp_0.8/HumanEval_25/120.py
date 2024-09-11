Here is the self-contained Python script that solves the problem:
```python
from typing import List

def factorize(n: int) -> List[int]:
    """
    Return list of prime factors of given integer in the order from smallest to largest.
    Each of the factors should be listed number of times corresponding to how many times it appears in factorization.
    Input number should be equal to the product of all factors

    Args:
        n (int): The number to factorize.

    Returns:
        List[int]: A list of prime factors.
    """
    factors = []
    i = 2
    while n > 1:
        if n % i == 0:
            n = n // i
            factors.append(i)
        else:
            i += 1
    return factors

# Test cases
if __name__ == "__main__":
    test_cases = [
        (8, [2, 2, 2]),
        (25, [5, 5]),
        (70, [2, 5, 7])
    ]

    for n, expected in test_cases:
        result = factorize(n)
        assert result == expected, f"Expected factorize({n}) to return {expected}, but got {result}"
    print("All test cases passed!")
```
This script uses a simple algorithm to find the prime factors of a given number `n`. It repeatedly divides `n` by the smallest prime number `i` (starting from 2) until `n` is no longer divisible by `i`. The result is a list of prime factors, each listed the number of times it appears in the factorization. The test cases at the end of the script verify that the function works correctly.