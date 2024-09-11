### Prime Factorization Script
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
    List[int]: A list of prime factors of the input number.
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
    print(factorize(8))  # [2, 2, 2]
    print(factorize(25))  # [5, 5]
    print(factorize(70))  # [2, 5, 7]
```

### Explanation:
- The function `factorize(n)` uses a while loop to divide the input number `n` by the smallest divisor `i` (starting from 2) until `n` is no longer divisible by `i`.
- If `n` is no longer divisible by `i`, `i` is incremented by 1.
- The quotient of each division is replaced by the divisor, so that we are effectively dividing `n` by the smallest prime factor at each step.
- Once the loop finishes, if `n` is greater than 1, it means that `n` itself is a prime factor and we append it to the list of factors.
- The function finally returns the list of prime factors.