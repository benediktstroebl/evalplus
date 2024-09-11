Here's a Python script that uses a simple algorithm to factorize a given number into its prime factors:

```markdown
### Prime Factorization of a Given Number
#### Python Script

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

    def is_prime(num: int) -> bool:
        """ Helper function to check if a number is prime """
        if num < 2:
            return False
        for i in range(2, int(num ** 0.5) + 1):
            if num % i == 0:
                return False
        return True

    factors = []
    i = 2
    while i * i <= n:
        if n % i:
            # If i is not a divisor, increment it
            i += 1
        else:
            # If i is a divisor, divide n by i and add i to factors
            n //= i
            factors.append(i)
    if n > 1:
        # If n is a prime number greater than 1, add it to factors
        factors.append(n)
    return factors

# Test cases
print(factorize(8))  # Output: [2, 2, 2]
print(factorize(25))  # Output: [5, 5]
print(factorize(70))  # Output: [2, 5, 7]
```

This script defines a helper function `is_prime` to check if a number is prime, and then uses a loop to find the prime factors of the input number `n`. The prime factors are stored in the `factors` list and returned at the end of the function. The script also includes test cases to demonstrate the function's correctness.