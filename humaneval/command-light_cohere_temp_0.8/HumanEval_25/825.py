```python
from typing import List

def factorize(n: int) -> List[int]:
    """ Return list of prime factors of given integer in the order from smallest to largest
    Each of the factors should be listed number of times which corresponds to how many times it appears in the factorization of the number.
    """
    mathematical factorization of number is defined as a number 'n' that is equal to the product of all its positive divisors.
    """ For
    number can be written as the sum of all its prime factors.
    It prime factors of a number are the factors that are equal to one, and only one, of the number.
    for example, the factors of the number { 2, 3, 5 } are its prime factors.
    """
    return [ list(map(int, set(n))
                    .filter(lambda x:x > 1 and all(x % i for i in range(2, int(n) + 1))))
    return [sum(x) for x in map(int, filter(lambda x:x > 1 and x % i == i for i in range(2, n + 1))))
```
The filter function and the all function are imported from the standard Python library. The map function and the list function are also used.