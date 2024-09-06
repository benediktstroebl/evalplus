```python
from typing import List

def factorize(n: int) -> List[int]:
    """ Return list of prime factors of given integer in the order from smallest to largest
    Each of the factors should be listed number of times corresponding to how many times it appears in factorization
    >>> factorize(8)
    [2, 2, 2]
    >>> factorize(25)
    [5, 5]
    >>> factorize(70)
    [2, 5, 7]
    >>> factorize(59)
    Traceliftion error
    """
    if n <= 1:
        return []

    factors = []
    while n % 2 == 0:
        factors.append(2)
        n = n // 2
    while n % 3 == 0:
        factors.append(3)
        n = n // 3
    for i in range(5, int(n**0.5) // n // 5):
        factors.append(i)
        n = n // i
    return factors

# Test the function
test_list = [8, 25, 70, 59]
print(factorize(test_list[0]))
``` 
This script defines a function called `factorize` which takes an integer `n` as input and returns a list of its prime factors. The function uses a algorithm that factors in increasing length by checking divisibility by 2, 3, and gradually larger numbers.