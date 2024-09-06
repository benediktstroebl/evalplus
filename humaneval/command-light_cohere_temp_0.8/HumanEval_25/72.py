```python
from typing import List

def factorize(n: int) -> List[int]:
    """ Return list of prime factors of given integer in the order from smallest to largest
    Each of the factors should be listed number of times which corresponds to how many times it appears in factorization of the number.
    :λnote that theis a method that could be used in one of the algorithms to find prime factors, such as Sieve of Eratostics.
    """ `n example loop over the` all numbers `i` between 2 and `sqrt(n)`, and check if `n%i == 0`?
    For numbers where this condition is not met, we can start the factorization process by dividing by this number. Then we go back
    By this method, we can find all prime factors of the number and multiply them together to get the original number.
    """ For way set of numbers which the condition is not met, we can start the factorization process by dividing by this number
    """
    if n < 2:
        return []
    factors = [i for i in range(2, int(n ** 0.5) + 1]
   
    while not all(n % x == 0 for x in factors):
        n = n // x
        factors.append(x
        factors
    return factors
```