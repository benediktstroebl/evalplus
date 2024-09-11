Here's a Python script that uses a prime factorization approach to solve the problem:
```markdown
### Prime Factorization

#### Description

This script calculates the prime factors of a given integer and returns them as a list.

#### Code

```python
from typing import List

def factorize(n: int) -> List[int]:
    """Return list of prime factors of given integer in the order from smallest to largest.
    Each of the factors should be listed number of times corresponding to how many times it appears in factorization.
    Input number should be equal to the product of all factors
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
    print(factorize(8))  # Output: [2, 2, 2]
    print(factorize(25))  # Output: [5, 5]
    print(factorize(70))  # Output: [2, 5, 7]
```

#### Explanation

This script uses a simple trial division approach to find the prime factors of a given integer. It starts by dividing the number by 2 (the smallest prime number), and continues dividing by increasing integers until it finds a non-divisor. If the number is not divisible, it increments the divisor by 1. If the number is divisible, it divides the number by the divisor and adds it to the list of factors. This process continues until the number is reduced to 1. The final list of factors is then returned.

This approach is simple and efficient, as it only requires a single pass through the numbers from 2 to the square root of the input number.