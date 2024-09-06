```python
from typing import List

def factorize(n: int) -> List[int]:
    factors = []
    while n > 1:
        if n % 2 == 0:
            factors.append(2)
        n //= 2
    else:
        for i in range(3, int(n**0.5) + 1,):
            if n % i == 0:
                factors.append(i)
                n //= i
    return factors

# Test the function
def test_factorize():
    assert factorize(8) == [2, 2, 2]
    assert factorize(25) == [5, 5]
    assert factorize(70) == [2, 5, 7]
```
This script defines a function 'factorize' that takes an integer 'n' as input and returns a list of its prime factors. It uses a test loop and constant factorization methods to find the prime factors of 'n'.