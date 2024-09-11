```python
from typing import List

def factorize(n: int) -> List[int]:
    """
    Return list of prime factors of given integer in the order from smallest to largest.
    Each of the factors should be listed number of times corresponding to how many times it appears in factorization.
    Input number should be equal to the product of all factors.

    :param n: The number to factorize
    :return: A list of prime factors
    """

    def is_prime(x: int) -> bool:
        """
        Check if a number is prime.

        :param x: The number to check
        :return: True if the number is prime, False otherwise
        """
        if x < 2:
            return False
        for i in range(2, int(x ** 0.5) + 1):
            if x % i == 0:
                return False
        return True

    factors = []
    i = 2
    while i * i <= n:
        if n % i:
            i += 1
        else:
            n //= i
            factors.append(i)
    if n > 1:
        factors.append(n)
    return factors


# Test cases
assert factorize(8) == [2, 2, 2]
assert factorize(25) == [5, 5]
assert factorize(70) == [2, 5, 7]

if __name__ == "__main__":
    print(factorize(8))  # Output: [2, 2, 2]
    print(factorize(25))  # Output: [5, 5]
    print(factorize(70))  # Output: [2, 5, 7]
```

This script defines the `factorize` function, which takes an integer as input and returns a list of its prime factors. The function uses a helper function `is_prime` to check if a number is prime, but actually it does not need it.

The function iterates through numbers from 2 to the square root of the input number, dividing the input number by each number that it is divisible by. If the input number is no longer divisible by any of these numbers, it is itself a prime number and is added to the list of factors.

The script also includes test cases to verify that the function works correctly.