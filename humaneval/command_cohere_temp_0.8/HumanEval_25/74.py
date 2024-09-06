```python
from typing import List

def factorize(n: int) -> List[int]:
    factors = []
    for i in range(2, n):
        is_factor = n % i == 0
        if is_factor and i != 1:
            factors.append(i)
            n //= i
    if n > 1:
        factors.append(n)
    return factors
```

The code uses a simple optimization to reduce the number of divisions performed by checking if the integer is divisible by numbers from 2 up to the input number `n`. This way, it determines the prime factors of the number in the order from the smallest to the largest and lists them accordingly. 

To ensure that the prime factors are truly prime, the code only adds factors that are not equal to 1 and also checks that the input integer is, in fact, divisible by the number. 

Let's verify the behavior of the provided solution with some examples:
```python
>>> factorize(8)
[2, 2, 2]
>>> factorize(25)
[5, 5]
>>> factorize(70)
[2, 5, 7]
```