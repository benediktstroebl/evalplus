```python
from typing import List

def factorize(n: int) -> List[int]:
    factors = []
    while n > 1:
        if n % 2 == 0:
            factors.append(2)
        n //= 2
    else:
        i = 3
        while i * i <= n:
            if n % i == 0:
                factors.append(i)
                n //= i
        else:
            i += 2
    return factors
``` 
This script defines a function called factorize, which takes an integer n as input and returns a list of its prime factors. The function uses a systematic method of factoring by checking divisibility, starting from 2 and moving up in multiples of 2 until the number becomes odd. 

This function effectively identifies and organizes the prime factors of the given number.