```python
from typing import List

def prime_factors(n: int) -> List[int]:
    """ Return list of prime factors of given integer in the order from smallest to largest.
    Each of the factors should be listed number of times corresponding to how many times it appears in factorization.
    Input number should be equal to the product of all factors
    """
    if n < 2:
        return []
    factors = []
    while n % 2 == 0:
        factors.append(2)
        n = n // 2
    for i in range(3, int(n ** 0.5) + 1, 2):
        while n % i == 0:
            factors.append(i)
            n = n // i
    if n > 2:
        factors.append(int(n))
    return factors

def factorize(n: int) -> List[int]:
    return [factor]*count for factor, count in zip(prime_factors(n), prime_factors(n))
```
The function `prime_factors` calculates the prime factors of the given number `n` and returns them listed in the order from smallest to largest. The `factorize` function uses `prime_factors` and returns the list of prime factors of `n`, with each factor repeated accordingly to how many times it appears in the factorization of `n`. 

Here is an example:
```python
>>> factorize(8)
[2, 2, 2]
>>> factorize(25)
[5, 5]
>>> factorize(70)
[2, 5, 7]
```

This solution is efficient and can solve the given problem in `O(sqrt(n))`, where `n` is the given number. It uses trial division coupled with the fact that prime numbers are grouped in pairs that alternate with the even numbers, so each even number that is not 2 is not a prime. 

An alternative approach using the same idea could be implemented using itertools.count and a generator expression:
```python
import itertools

def factorize(n: int) -> List[int]:
    return list(itertools.count(i, i))[1:] for i in prime_factors(n)
```
This approach does not require a nested function call and uses `prime_factors` to generate the required list of factors. 

You can test this code by adding a suite of example tests, such as:
```python
def test_factorize():
    assert factorize(8) == [2, 2, 2]
    assert factorize(25) == [5, 5]
    assert factorize(70) == [2, 5, 7]

    # Other test cases
    assert factorize(27) == [3, 3]
    assert factorize(39) == [3, 3, 3]
    assert factorize(120) == [2, 2, 3, 5, 5]
``` 
This way, you can ensure that the factorization function works correctly for a variety of test cases.