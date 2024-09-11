```python
from typing import List

def factorize(n: int) -> List[int]:
    """
    Return list of prime factors of given integer in the order from smallest to largest.
    Each of the factors should be listed number of times corresponding to how many times it appears in factorization.
    Input number should be equal to the product of all factors

    Args:
        n (int): Number to factorize

    Returns:
        List[int]: List of prime factors
    """
    def is_prime(num: int) -> bool:
        """Check if number is prime"""
        if num < 2:
            return False
        for i in range(2, int(num ** 0.5) + 1):
            if num % i == 0:
                return False
        return True

    factors = []
    divisor = 2
    while n > 1:
        if n % divisor == 0:
            if is_prime(divisor):
                factors.append(divisor)
                n //= divisor
            else:
                divisor += 1
        else:
            divisor += 1
    return factors


# Test cases
print(factorize(8))  # [2, 2, 2]
print(factorize(25))  # [5, 5]
print(factorize(70))  # [2, 5, 7]
```
This solution works by dividing the input number `n` by the smallest divisor (starting from 2) until it is no longer divisible. If the divisor is a prime number, it is added to the list of factors. The process continues until `n` is reduced to 1.

However, the solution can be improved by not checking if the divisor is prime inside the while loop. Here's a revised solution:

```python
from typing import List

def factorize(n: int) -> List[int]:
    """
    Return list of prime factors of given integer in the order from smallest to largest.
    Each of the factors should be listed number of times corresponding to how many times it appears in factorization.
    Input number should be equal to the product of all factors

    Args:
        n (int): Number to factorize

    Returns:
        List[int]: List of prime factors
    """
    factors = []
    divisor = 2
    while divisor * divisor <= n:
        while n % divisor == 0:
            factors.append(divisor)
            n //= divisor
        divisor += 1
    if n > 1:
        factors.append(n)
    return factors


# Test cases
print(factorize(8))  # [2, 2, 2]
print(factorize(25))  # [5, 5]
print(factorize(70))  # [2, 5, 7]
```
This solution works similarly, but instead of checking if the divisor is prime, it simply increments the divisor until it is no longer a divisor of `n`. This approach is more efficient and avoids unnecessary prime checks.