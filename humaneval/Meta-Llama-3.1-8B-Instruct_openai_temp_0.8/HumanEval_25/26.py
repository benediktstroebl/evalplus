```markdown
### Factorize Function

#### Description
Returns a list of prime factors of a given integer in the order from smallest to largest.
Each of the factors is listed the number of times corresponding to how many times it appears in the factorization.
The input number should be equal to the product of all factors.

#### Function

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

    def prime_factors(n: int) -> int:
        """Check if a number is prime."""
        if n <= 1:
            return False
        for i in range(2, int(n**0.5) + 1):
            if n % i == 0:
                return False
        return True

    factors = []
    i = 2
    while i * i <= n:
        if n % i:
            i += 1
        else:
            n //= i
            if prime_factors(i):
                factors.append(i)
    if n > 1 and prime_factors(n):
        factors.append(n)
    return factors


# Example use cases
if __name__ == "__main__":
    print(factorize(8))  # Output: [2, 2, 2]
    print(factorize(25))  # Output: [5, 5]
    print(factorize(70))  # Output: [2, 5, 7]
```

#### Explanation
The `factorize` function takes an integer `n` as input and returns a list of its prime factors.
The function uses a helper function `prime_factors` to check if a number is prime.
The main function iterates through numbers from 2 to the square root of `n` and checks for divisibility.
If `n` is divisible by a number `i`, it appends `i` to the list of factors and divides `n` by `i`.
Finally, if `n` is a prime number greater than 1, it appends `n` to the list of factors.
The function returns the list of prime factors.
The example use cases demonstrate the function's behavior for different inputs.