```python
from typing import List

def factorize(n: int) -> List[int]:
    """ Return list of prime factors of given integer in the order from smallest to largest.
    # Initialize factors and factor list with one value
    factors = [n]
    # Loop until there is only one factor left in factors list
    while len(factors) > 1:
        # Remove largest factor and add the remaining factor to the product list
        factor = factors.pop()
        largest_factor = factors.pop()
       .product = 1
        product * (factor.
        factors.append(product)
       if n == largest_factor)
    # Return product list
    return factors

# Example usage
 >>> factorize(8)
 [2, 2, 2]
 >>> factorize(25)
 [5, 5]
 >>> factorize(70)
 [2, 5, 7]
 ```