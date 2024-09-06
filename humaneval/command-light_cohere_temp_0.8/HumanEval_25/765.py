```python
from typing import List

def factorize(n: int) -> List[int]:
    """ Return list of prime factors of given integer in the order from smallest to largest
    Each of the factors should be listed number of times, which corresponds to how many it appears in factorization
    Input number should be equal to the product of all the factors returned
    """
    factors = []
    for i in range(2, int(n**0.5) + 1):
        while n % i == 0:
            factors.append(i)
            n //= i
            if len(factors) == i:
                break
    return factors

# Test cases
print(factorize(8))  # [2, 2, 2]
print(factorize(25))  # [5, 5]
print(factorize(70))  # [2, 5, 7]
 ``` 
This function, factorize, takes an integer n as input and returns a list of prime factors of that number. It starts by generating a smallest prime factor and adds it to the factors list. Then, it checks whether this prime factor can divide n, which is the next factor. If not, it has found all prime factors of n, and that's the end of the loop.