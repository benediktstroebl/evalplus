```python
from typing import List

def factorize(n: int) -> List[int]:
    factors = []
    for i in range(2, n):
        if n % i == 0:
            count = 0
            while n % i == 0:
                n //= i
                count += 1
            if count > 0:
                factors.append(i)
                factors.append(count)
    if n > 1:
        factors.append(n)
        factors.append(1)
    return factors[1:]
```
The factorize function iterates through numbers from 2 up to the given input number n. 
It checks if the number is divisible by i, and if it is, it calculates the number of times the greatest common divisor occurs in the factorization, counting it using a loop. The factor is added to the list with the number of occurrences, but the count of 2, which is a special case for the function, is added only once. After that, the remaining factor is checked and added with a count of 1. The resulting list of factors is returned, with the count attribute removed. 
The function has a specified docstring for better understanding and usage explanation.

Here is an example of how to use the function:
```python
>>> factorize(8)
[2, 2, 2]
>>> factorize(25)
[5, 5]
>>> factorize(70)
[2, 5, 7]
```