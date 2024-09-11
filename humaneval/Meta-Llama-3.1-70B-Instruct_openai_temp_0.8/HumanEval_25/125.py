```python
from typing import List

def factorize(n: int) -> List[int]:
    """
    Return list of prime factors of given integer in the order from smallest to largest.
    Each of the factors should be listed number of times corresponding to how many times it appeares in factorization.
    Input number should be equal to the product of all factors

    Args:
        n (int): The input integer to be factorized.

    Returns:
        List[int]: A list of prime factors in ascending order, with each factor repeated according to its multiplicity.
    """
    def is_prime(num: int) -> bool:
        """
        Helper function to check if a number is prime.

        Args:
            num (int): The number to be checked.

        Returns:
            bool: True if the number is prime, False otherwise.
        """
        if num < 2:
            return False
        for i in range(2, int(num ** 0.5) + 1):
            if num % i == 0:
                return False
        return True

    factors = []
    for i in range(2, n + 1):
        if is_prime(i):
            while n % i == 0:
                factors.append(i)
                n //= i
    return factors


# Test cases
print(factorize(8))   # [2, 2, 2]
print(factorize(25))  # [5, 5]
print(factorize(70))  # [2, 5, 7]
```

This script defines a function `factorize` that takes an integer `n` as input and returns a list of its prime factors in ascending order. The function uses a helper function `is_prime` to check if a number is prime.

Here's a step-by-step explanation of how the script works:

1.  The `is_prime` function checks if a number is prime by iterating from 2 to the square root of the number and checking for divisibility. If the number is divisible by any of these values, it's not prime.
2.  The `factorize` function iterates from 2 to the input number `n`.
3.  For each number `i` in this range, it checks if `i` is prime using the `is_prime` function.
4.  If `i` is prime, it checks if `n` is divisible by `i`. If it is, it appends `i` to the `factors` list and divides `n` by `i`. This process repeats until `n` is no longer divisible by `i`.
5.  The function returns the `factors` list, which contains the prime factors of the original input number in ascending order, with each factor repeated according to its multiplicity.

The test cases at the end of the script demonstrate the function's correctness by comparing its output with the expected output for different input values.