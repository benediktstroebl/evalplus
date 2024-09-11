### Prime Factorization of an Integer
### =================================

Below is a Python script that implements a function to calculate the prime factorization of a given integer.

```markdown
### Python Script
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
        List[int]: A list of prime factors in the order from smallest to largest.
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

### Example Usage
if __name__ == "__main__":
    print(factorize(8))  # [2, 2, 2]
    print(factorize(25))  # [5, 5]
    print(factorize(70))  # [2, 5, 7]
```

### Explanation
This script uses a simple method to find prime factors. It starts from the smallest prime number (2) and checks if the given number is divisible by it. If it is, it adds the factor to the list and divides the number by the factor. It continues this process until the number is reduced to 1. If at any point the number is not divisible by the current factor, it increments the factor by 1. This ensures that the function finds all prime factors in the correct order.

The function returns a list of prime factors in the order from smallest to largest. Each factor appears in the list the number of times it appears in the factorization of the input number.