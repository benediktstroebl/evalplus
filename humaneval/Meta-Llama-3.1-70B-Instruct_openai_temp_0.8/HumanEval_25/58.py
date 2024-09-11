```python
from typing import List

def factorize(n: int) -> List[int]:
    """
    Return list of prime factors of given integer in the order from smallest to largest.
    Each of the factors should be listed number of times corresponding to how many times it appeares in factorization.
    Input number should be equal to the product of all factors
    
    :param n: Input integer to factorize
    :return: List of prime factors
    """
    factors = []
    i = 2
    while n > 1:
        if n % i == 0:
            factors.append(i)
            n = n // i
        else:
            i += 1
    return factors

# Test cases
assert factorize(8) == [2, 2, 2]
assert factorize(25) == [5, 5]
assert factorize(70) == [2, 5, 7]
```

This script works by dividing the input number `n` by the smallest possible divisor `i`, starting from 2, until it is no longer divisible. The divisor is then added to the list of factors and the process is repeated with the remaining quotient until it is reduced to 1. The result is a list of prime factors in ascending order, each repeated according to its multiplicity in the factorization. 

Note that this implementation does not require any external libraries or complex mathematical operations, making it efficient and straightforward.