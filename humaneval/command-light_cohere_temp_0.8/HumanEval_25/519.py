```python
from typing import List
def factorize(n: int) -> List[int]:
    factors = []
    while n % 2 == 0:
        factors.append(2)
        n = n // 2
    for i in range(3, int(n**0.5) + 1, step = 2**i:
        while n % step == 0:
            factors.append(step)
            n = n // step
    factors.append(n)
    return factors
def test_factorize():
    assert factorize(8) == [2, 2, 2]
    assert factorize(25) == [5, 5]
    assert factorize(70) == [2, 5, 7]
```  The code defines a function that takes an integer n as input and returns a list of prime factors of that number. The function works by first finding the smallest prime factor of n, which is 2 in all cases. Then, it iterates through i from 3 to the square root of n, and for each step, it finds the smallest prime factor that divides n evenly. The function then adds this factor to the list of factors.