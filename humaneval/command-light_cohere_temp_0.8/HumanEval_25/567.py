```python
from typing import List

def factorize(n: int) -> List[int]:
    """ Return list of prime factors of given integer in the order from smallest to largest.
    Ifs print function can be used to print out the solution, which is a list of prime factors.
    """
    list comprehension is used to find the prime factors of the number, and the filter function is used to keep only the factors that are greater than or equal to the square root of the number.
    Return: The function can be used to solve the problem for any given integer n.  """
 def test_factorize(n: int) -> None:
    if n < 2:
        return
    factors = factorize(n)
    if len(factors) == 1:
        return "Error: number has no prime factors"
    return factors
```