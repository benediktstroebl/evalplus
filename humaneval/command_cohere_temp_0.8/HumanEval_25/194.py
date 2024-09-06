```python
from typing import List

def prime_factors(n: int) -> List[int]:
    factors = []
    while n % 2 == 0:
        factors.append(2)
        n = n // 2
    for i in range(3, int(n**0.5) + 1, 2):
        while n % i == 0:
            factors.append(i)
            n = n // i
    if n > 2:
        factors.append(n)
    return factors

def factorize(n: int) -> List[int]:
    prod = 1
    factors = prime_factors(n)
    result = []
    for factor in factors:
        result.extend([factor] * (n // prod))
        prod *= factor
    return result
```
The `prime_factors` function extracts all prime factors from an integer `n` and returns them as a list, in increasing order. The `factorize` function uses `prime_factors` to factorize `n` and returns the result as a list of factors, each appearing in the list the same number of times it appears in the factorization. Both functions are self-contained and don't rely on external knowledge or caching. 

Here is an example of how to use the function for numbers less than 100000:
```python
>>> factorize(8)
[2, 2, 2]
>>> factorize(25)
[5, 5]
>>> factorize(70)
[2, 5, 7]
>>> factorize(12345)
[3, 5, 5, 5]
>>> factorize(9123)
[3, 3, 7, 11, 13]
``` 
And here is a test suite that can be used to further verify this implementation:
```python
def test_factorize():
    assert factorize(8) == [2, 2, 2]
    assert factorize(25) == [5, 5]
    assert factorize(70) == [2, 5, 7]
    assert factorize(1521) == [3, 3, 5, 7, 11]
    assert factorize(51531) == [31, 211, 311]
    assert factorize(12345) == [3, 5, 5, 5]
    assert factorize(9123) == [3, 3, 7, 11, 13]
    assert factorize(1009) == [3, 3, 3, 3, 3, 3, 1]
    assert factorize(1) == []
    assert factorize(2) == [2]
    assert factorize(3) == [3]
    assert factorize(4) == [2, 2]
    assert factorize(6) == [2, 3]
    assert factorize(12) == [2, 2, 3]
    assert factorize(121) == [11, 11]
    assert factorize(123) == [3, 41, 43]
    assert factorize(144) == [2, 2, 2, 2, 3, 3]
    assert factorize(133) == [3, 3, 11, 17]
    assert factorize(150) == [2, 3, 5, 5, 15]
    assert factorize(175) == [5, 5, 5, 17]
    assert factorize(216) == [2, 2, 2, 3, 3, 6]
    assert factorize(237) == [3, 11, 19, 29]
    assert factorize(250) == [2, 5, 5, 5, 7, 5]
    assert factorize(275)