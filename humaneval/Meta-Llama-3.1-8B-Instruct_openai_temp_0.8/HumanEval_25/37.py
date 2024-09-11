```python
from typing import List
import math

def factorize(n: int) -> List[int]:
    """
    Return list of prime factors of given integer in the order from smallest to largest.
    Each of the factors should be listed number of times corresponding to how many times it appears in factorization.
    Input number should be equal to the product of all factors

    Args:
        n (int): The input number to be factorized.

    Returns:
        List[int]: A list of prime factors of the input number.
    """
    factors = []
    # Find the square root of the number
    i = 2
    while i * i <= n:
        # If the number is divisible by i, then i is a factor
        if n % i:
            # If the number is not divisible by i, increment i by 1
            i += 1
        else:
            # If the number is divisible by i, divide the number by i and add i to the factors list
            n //= i
            factors.append(i)
    # If the number is greater than 1, then it is a prime number and should be added to the factors list
    if n > 1:
        factors.append(n)
    # Return the list of factors
    return factors

# Test the function
print(factorize(8))  # [2, 2, 2]
print(factorize(25))  # [5, 5]
print(factorize(70))  # [2, 5, 7]
```

This script uses a while loop to iterate through numbers from 2 to the square root of the input number, checking if the number is divisible by the current number. If it is, the loop divides the number by the current number and adds it to the list of factors. This process continues until the number is reduced to 1, at which point the list of factors is returned. If the number is a prime number greater than 1, it is added to the list of factors.