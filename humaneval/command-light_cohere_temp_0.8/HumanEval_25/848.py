```python
from typing import List

def factorize(n: int) -> List[int]:
    """ Return list of prime factors of given integer in the order from smallest to largest.
    Input number is n is the product of all factors.
    The function loops through numbers 2 to the square root of n and checks if it is divisible by n, if it is, it is added to the list.
    """
    list of factors will be in ascending order and corresponding to how many times they appear in factorization.
"""

def main() -> None:
    n = 25
    factors = factorize(n)
    print(factors)
    ```