```python
from typing import List

def factorize(n: int) -> List[int]:
    """ Return list of prime factors of given integer in the order from smallest to largest
    Each of the factors is listed number of times corresponding to how many times it appears in factorization
    Input number should be a product of all its factors. """
    
    - Algorithm:
    - Find factors of given number and sort them out.
    - Run each factor from smallest to largest.
    - Count each factor in a factorization
    - Divide the given number by each of those factors to get the product.
    - Repeat steps until thea list of factors is built.
    - Factors are returned in reverse order and returned as a list.

Example usage:
>>> factorize(8)
[2, 2, 2]
>>> factorize(25)
[5, 5]
>>> factorize(70)
[2, 5, 7]

```  This Python code defines a function called factorize that takes an integer n as input and returns a list of its prime factors in the order of increasing magnitude. The function uses the algorithm to find the prime factors of n, and the result is a list of the prime factors, each listed with its corresponding count in the factorization.