```python
from typing import List

def factorize(n: int) -> List[int]:
    """
    Return list of prime factors of given integer in the order from smallest to largest.
    Each of the factors should be listed number of times corresponding to how many times it appears in factorization.
    Input number should be equal to the product of all factors
    
    Parameters:
    n (int): The number to be factorized
    
    Returns:
    List[int]: A list of prime factors of the input number
    """
    i = 2
    factors = []
    while i * i <= n:
        if n % i:
            i += 1
        else:
            n //= i
            factors.append(i)
    if n > 1:
        factors.append(n)
    return factors

# Test the function
print(factorize(8))   # [2, 2, 2]
print(factorize(25))  # [5, 5]
print(factorize(70))  # [2, 5, 7]
```

This script uses a simple trial division method to find the prime factors of a number. It starts by checking divisibility from 2 and increments the divisor until it finds one that divides the number, then it continues dividing the number by that divisor until it can no longer do so. It repeats this process until the number being divided is reduced to 1. The list of divisors found is the list of prime factors, which is then returned by the function.