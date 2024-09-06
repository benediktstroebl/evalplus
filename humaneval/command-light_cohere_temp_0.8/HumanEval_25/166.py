```python
from typing import List

def factorize(n: int) -> List[int]:
    """ Return list of prime factors of given integer in the order from smallest to largest.
    If a list comprehension method:
    - Iterate over numbers from 2 to the square root of n
    - If the current number is divisible by any number in the range, it is not a prime number and removed from the list.
    - Keep loop until all number is no longer divisible
    """
    factors = []
    while n != 1:
        for i in range(2, int(n**0.5)):
            if n % i == 0:
                factors.append(i)
                n = n / i
    factors.append(n)
    return factors

# Example Test:
print(factorize(8))
print(factorize(25))
print(factorize(70))
 ```

This Python script defines a function called factorize, which takes an integer n as input and returns a list of prime factors of n in descending order. The function uses a list comprehension method, iterating over the numbers from 2 up to the square root of n and checking if n is divisible by any of these numbers. If n is divisible by any of them, it is not a prime number and that number is removed from the list of factors. The function continues until n becomes 1, at which point it has found all the prime factors of n.