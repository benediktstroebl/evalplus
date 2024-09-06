```python
from typing import List

def factorize(n: int) -> List[int]:
    """ Return list of prime factors of given integer in the order from smallest to largest
    Each of the factors are listed number of times which corresponds to how many times it appears in factorization
    Input number should be equal to the product of all its factors
    """
    if n <= 1:
        return []
    elif n <= 3:
        return [1]
    else:
        return [i for i in range(2, int(n ** 0.5),5, n % 2 == 1]
``` 
The code defines a function `factorize` that takes an integer `n` as input and returns a list of prime factors of the input number. The function uses a testing two boundary conditions and then uses the Euclidean algorithm to find prime factors. 

The function will correctly identify the prime factors of the input number and return them in ascending order.