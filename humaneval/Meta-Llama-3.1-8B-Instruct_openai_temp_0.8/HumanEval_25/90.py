### Prime Factorization Script in Python

Below is a Python script that implements the prime factorization function as described.

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
        n (int): The number to be factorized.

    Returns:
        List[int]: A list of prime factors.
    """
    factors = []
    i = 2
    while n > 1:  # continue until n is reduced to 1
        if n % i == 0:  # if n is divisible by i
            n = n // i  # divide n by i
            factors.append(i)  # add i to the factors list
        else:
            i += 1  # increment i to check the next number
    return factors

# Example usage
print(factorize(8))  # [2, 2, 2]
print(factorize(25))  # [5, 5]
print(factorize(70))  # [2, 5, 7]
```

### Explanation

*   The `factorize` function takes an integer `n` as input and returns a list of prime factors.
*   The function starts from `2` (`i = 2`) and checks if `n` is divisible by `i`.
*   If `n` is divisible by `i`, `n` is divided by `i`, and `i` is added to the factors list.
*   If `n` is not divisible by `i`, `i` is incremented by `1`, and the next number is checked.
*   This process continues until `n` is reduced to `1`.
*   The list of factors is then returned.

This script effectively factorizes the input number into its prime factors while maintaining the order from smallest to largest and preserving the frequency of each factor.