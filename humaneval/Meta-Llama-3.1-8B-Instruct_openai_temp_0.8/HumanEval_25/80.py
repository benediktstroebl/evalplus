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
    
    factors = []
    i = 2
    
    # Start from 2 and divide n by i while i divides n
    while i * i <= n:
        if n % i:
            # If i doesn't divide n, increment i by 1
            i += 1
        else:
            # If i divides n, append i to the list of factors and divide n by i
            n //= i
            factors.append(i)
    
    # If n is greater than 1, it means n itself is a prime factor
    if n > 1:
        factors.append(n)
    
    return factors

# Example usage
print(factorize(8))  # [2, 2, 2]
print(factorize(25))  # [5, 5]
print(factorize(70))  # [2, 5, 7]
```

In this script, the `factorize` function takes an integer `n` as input and returns a list of its prime factors. It uses a while loop to divide `n` by the smallest divisor `i` until `i` is greater than the square root of `n`. In each iteration, if `i` doesn't divide `n`, it increments `i` by 1. If `i` divides `n`, it appends `i` to the list of factors and divides `n` by `i`. Finally, if `n` is greater than 1, it means `n` itself is a prime factor, so it appends `n` to the list of factors. The script includes example usage at the end to demonstrate the function's behavior.