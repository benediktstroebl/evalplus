```python
from typing import List

def factorize(n: int) -> List[int]:
    """
    Return list of prime factors of given integer in the order from smallest to largest.
    Each of the factors should be listed number of times corresponding to how many times it appears in factorization.
    Input number should be equal to the product of all factors
    
    Args:
        n (int): A positive integer to be factorized
    
    Returns:
        List[int]: A list of prime factors of n
    
    Examples:
        >>> factorize(8)
        [2, 2, 2]
        >>> factorize(25)
        [5, 5]
        >>> factorize(70)
        [2, 5, 7]
    """
    
    # Initialize an empty dictionary to store prime factors and their counts
    factors = {}
    
    # Start checking from 2 (the smallest prime number)
    i = 2
    
    # Continue checking until we have checked all possible factors
    while i * i <= n:
        # If n is divisible by i, it means i is a prime factor
        if n % i:
            # If n is not divisible by i, move to the next number
            i += 1
        else:
            # If n is divisible by i, divide n by i and increment the count of i in the dictionary
            n //= i
            factors[i] = factors.get(i, 0) + 1
    
    # If n is a prime number greater than 1, it is the last prime factor
    if n > 1:
        factors[n] = factors.get(n, 0) + 1
    
    # Convert the dictionary into a list in ascending order and return it
    return sorted([k for k, v in factors.items() for _ in range(v)])

# Test the function
print(factorize(8))  # [2, 2, 2]
print(factorize(25))  # [5, 5]
print(factorize(70))  # [2, 5, 7]
```

This script uses a dictionary to store prime factors and their counts, then converts the dictionary into a list in ascending order before returning it. The function `factorize` takes an integer `n` as input, iterates from 2 to the square root of `n`, and checks for divisibility. If `n` is divisible by a number, it divides `n` by that number and increments the count of that number in the dictionary. After checking all numbers, if `n` is greater than 1, it means `n` is a prime number, and we add it to the dictionary. Finally, we convert the dictionary into a list in ascending order and return it.