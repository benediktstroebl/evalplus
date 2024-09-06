```python
from typing import List
def factorize(n: int) -> List[int]:
    """ Return list of prime factors of given integer in the order from smallest to largest
    Each of the factors is listed number of times, which corresponds to how many times it appears in the factorization of the given number.
    Input number should be equal to the product of all factors"""
    factors = []
    while n % 2 == 0:
        factors.append(2)
        n = n // 2
    i = 3
    while i * i <= n:
        if n % i == 0:
            factors.append(i)
            n = n // i
        i += 2
    for j in factors:
        if j > 1:
            factors.append(factors[0] * j)
    return factors
# Example usage
print(factorize(8))
print(factorize(25))
print(factorize(70))
``` 
This script defines a function called `factorize` that takes an integer `n` as input and returns a list of its prime factors. The function uses a loop to find all the prime factors of the number, starting with the factors of 2 and 3, and then factors of the form `prime(base `i`) where `i` is the square root of the number of factors of 2 and 3. The function then checks if the factor is divisible by the input number and, if it is, appends it to the list of factors.