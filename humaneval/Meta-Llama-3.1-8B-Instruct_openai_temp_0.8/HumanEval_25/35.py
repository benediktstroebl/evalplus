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
    List[int]: A list of prime factors
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

# Test cases
print(factorize(8))  # [2, 2, 2]
print(factorize(25))  # [5, 5]
print(factorize(70))  # [2, 5, 7]
```

This script uses a simple trial division method to find the prime factors of the given number. It starts by dividing the number by 2, and if it's divisible, it adds 2 to the list of factors and divides the number by 2. It continues this process with increasing integers until the square of the current integer exceeds the number. If the number is still greater than 1 at this point, it means that the number is a prime number and is added to the list of factors. The script then returns the list of factors.