```python
from typing import List

def factorize(n: int) -> List[int]:
    factors = []
    while n % 2 == 0:
        factors.append(2)
        n = n // 2
    for i in range(3, int(n**0.5) + 1, steps=2):
        while n % i == 0:
            factors.append(i)
            n = n // i
    factors.append(n)
    return factors
```
This function, factorize, takes an integer n as input and returns a list of its prime factors. The function uses a 'while' loop to repeatedly divide by the least prime factor until the number is divisible by 2 or larger. It then checks each prime factor by iterating from 3 up to the square root of the input number, in steps of 2. 

The function also uses a 'for' loop to find all prime factors of the number. 

Finally, it returns the list of prime factors in order from smallest to largest.