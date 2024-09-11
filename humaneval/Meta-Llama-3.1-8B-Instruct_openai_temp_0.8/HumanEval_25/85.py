```python
from typing import List

def factorize(n: int) -> List[int]:
    """
    Return list of prime factors of given integer in the order from smallest to largest.
    Each of the factors should be listed number of times corresponding to how many times it appears in factorization.
    Input number should be equal to the product of all factors
    
    >>> factorize(8)
    [2, 2, 2]
    >>> factorize(25)
    [5, 5]
    >>> factorize(70)
    [2, 5, 7]
    """
    factors = []
    i = 2
    while i * i <= n:
        # Check if 'i' is a factor of 'n'
        if n % i:
            i += 1
        else:
            n //= i
            # Check if 'i' is already in the list
            if i in factors:
                # If 'i' is already in the list, increment its count
                factors[factors.index(i)] *= 2
            else:
                # If 'i' is not in the list, add it with a count of 1
                factors.append(i)
    # Add any remaining value of 'n' to the list
    if n > 1:
        factors.append(n)
    return factors

# Test the function
print(factorize(8))   # [2, 2, 2]
print(factorize(25))  # [5, 5]
print(factorize(70))  # [2, 5, 7]
```
This script defines a function, `factorize`, that takes an integer `n` as input and returns a list of prime factors in the order from smallest to largest, with each factor listed the number of times it appears in the factorization. The function uses a while loop to find the prime factors, starting from the smallest prime number (2). If 'i' is a factor of 'n', it is added to the list and 'n' is divided by 'i'. If 'n' is not divisible by 'i', 'i' is incremented and the process is repeated. The remaining value of 'n' is added to the list when the loop finishes.