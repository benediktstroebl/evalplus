```python
from typing import List

def factorize(n: int) -> List[int]:
    """ Return list of prime factors of given integer in the order from smallest to largest
    Each of the factors should be listed in factorization order.
    Input number should be equal to the product of all factors
    >>> factorize(8)
    [2, 2, 2]
    >>> factorize(25)
    [5, 5]
    >>> factorize(70)
    [2, 5, 7]
    >>> factorize(15)
    Traceback (most recent call last):
      File "<stdin>", line 44, in <module>
        1: 'factorize'('15')'
    File "<stdin>", line 9, in factorize
        ^ Traceback (most recent call last):
          File "<stdin>", line 3, in <module>
            1: 'int'('15')'
            ^

    Invalid input: 15 is not a prime number
    """
    if n <= 1:
        return []
    elif n <= 3:
        return [n]
    elif n % 2 == 0:
        return [n, n * 2]
    else:
        factors = []
        for i in range(3, int(n ** 0.5), n //1):
            while n % i == 0:
                factors.append(i)
                n //= i
        return factors

```
Do you have any other questions related to Python programming or specific use cases you would like to discuss or explore further?