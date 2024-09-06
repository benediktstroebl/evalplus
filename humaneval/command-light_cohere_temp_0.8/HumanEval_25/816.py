```python
from typing import List

def factorize(n: int) -> List[int]:
    """
    Return list of prime factors of given integer in the order from smallest to largest
    each of which are listed number of times corresponding to how many times they appear in factorization
    """
    factors = []
    while n % 2 == 0:
        factors.append(2)
        n = n // 2
    for i in range(3, int(n ** 0.5) + 1, ]:
        is_prime = 1
        for j in range(2, int(i ** 0.5) + 1, i > j):
            if n % j == 0:
                is_prime = 0
                break
        if is_prime:
            factors.append(i)
        n = n // i
    return factors

# Test the function
print(factorize(8))
print(factorize(25))
print(factorize(70))
``` 
This code defines a function called `factorize` that takes an integer `n` as input and returns a list of its prime factors in order. It does this by iterating through the number 2 until the square root of `n`, checking for divisibility by each potential factor, and adding it to the list if it is a prime factor. The code then iterates from 3 to the square root of `n` with a step size of 2 and checks for divisibility by all potential factors from 2 to the square root of `n` onwards.