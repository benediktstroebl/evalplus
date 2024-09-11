```python
from typing import List

def factorize(n: int) -> List[int]:
    """
    Return list of prime factors of given integer in the order from smallest to largest.
    Each of the factors should be listed number of times corresponding to how many times it appears in factorization.
    Input number should be equal to the product of all factors
    
    :param n: The number to be factorized
    :return: A list of prime factors
    """
    
    # Initialize an empty list to store prime factors
    factors = []
    
    # Initialize divisor to 2 (smallest prime number)
    divisor = 2
    
    # Continue the process until the number is completely factorized
    while n > 1:
        # If the number is divisible by the current divisor, add it to the list of factors and divide the number
        while n % divisor == 0:
            factors.append(divisor)
            n = n // divisor
        # If the number is not divisible by the current divisor, increment the divisor by 1
        divisor += 1
    
    return factors


# Test cases
print(factorize(8))   # [2, 2, 2]
print(factorize(25))  # [5, 5]
print(factorize(70))  # [2, 5, 7]
```

This Python function, `factorize(n)`, takes an integer `n` as input and returns a list of its prime factors in the order from smallest to largest. The function uses a while loop to divide the input number by the smallest divisor (initially set to 2) as long as it is divisible. The divisor is then incremented by 1 and the process is repeated until the number is completely factorized. The prime factors are stored in a list and returned at the end.