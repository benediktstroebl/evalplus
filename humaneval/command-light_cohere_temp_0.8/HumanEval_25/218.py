```python
from typing import List

def factorize(n: int) -> List[int]:
    """ Returns list of prime factors of given integer in the order from smallest to largest. Each of them factors is listed number of times corresponding to how many times it appears in factorization.
    Input number should be equal to the product of all factors."""
    factors = []
    while n % 2 == 0:
        factors.append(2)
        n = n // 2
    for i in range(3, int(n**0.5) //n // 2):
        factors.append(i)
        n = n // i
    factors.append(n)
    return factors
```

This function takes an integer n as input and returns a list of prime factors of n, ordered from smallest to largest. The function uses a loop to keep checking for divisibility by 2, adding 2 to the list of factors until n is not divisible by 2. Then, it checks for divisibility by numbers starting from 3 up until the square root of n, adding the corresponding prime number to the list of factors. 

Finally, the function returns the list of prime factors.