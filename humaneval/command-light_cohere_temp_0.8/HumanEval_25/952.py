```python
from typing import List

def factorize(n: int) -> List[int]:
    """ Returns list of prime factors of given integer in the order from smallest to largest.
    Input number should be equal to the product of all factors
    """
    factors = []
    while n % 2 == 0:
        factors.append(2)
        n = n // 2
    for i in range(3, int(n**0.5) + 1, while n % i == 0:
        factors.append(i)
        n = n // i
    factors.append(int(n))
    return factors

# Test the function
def test_factorize() -> None:
    n = 8
    result = factorize(n)
    print(result)

# Test the function with a large number
n = 250000
    result = factorize(n)
    print(result)

# Test the function with a composite number
n = 6
    result = factorize(n)
    print(result)
``` 

This code defines a function factorize that returns a list of prime factors of a given integer. The function uses a well algorithm to find the prime factors, which is based on the observation that any odd number can be expressed as the product of two numbers from the set of odd primes less than 2 times. The function also handles tests to verify its correctness.