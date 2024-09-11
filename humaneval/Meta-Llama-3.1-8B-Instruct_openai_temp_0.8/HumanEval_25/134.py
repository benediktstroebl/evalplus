### Prime Factorization of Integer
#### Python Function to Find Prime Factors

```python
from typing import List

def factorize(n: int) -> List[int]:
    """
    Return list of prime factors of given integer in the order from smallest to largest.
    Each of the factors should be listed number of times corresponding to how many times it appears in factorization.
    Input number should be equal to the product of all factors
    
    Args:
    n (int): The input integer to find prime factors of.
    
    Returns:
    List[int]: A list of prime factors of the input integer.
    
    Examples:
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
        if n % i:
            i += 1
        else:
            n //= i
            factors.append(i)
    if n > 1:
        factors.append(n)
    return factors

# Example usage
print(factorize(8))  # Output: [2, 2, 2]
print(factorize(25))  # Output: [5, 5]
print(factorize(70))  # Output: [2, 5, 7]
```

This function uses a while loop to divide the input number `n` by the smallest divisor `i` until it is no longer divisible. The divisor `i` is then added to the list of factors and the process is repeated with the next possible divisor. When the loop finishes, the remaining number `n` is still greater than 1, it means `n` is a prime number, so it is added to the list of factors. The function returns the list of factors in the order from smallest to largest.