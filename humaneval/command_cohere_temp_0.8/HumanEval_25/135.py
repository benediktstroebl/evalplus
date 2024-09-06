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
The code uses a straightforward algorithm based on trial division. It iterates over numbers from 2 up to `n` and checks if they divide `n` without leaving a remainder. If a divisor is found, it iterates through the number's factors e.g. if `n` is 60 and it is divisible by 2, the code will factorize 2 into 2 x 2 x 3. If a number is not divisible by any integer greater than 1, it itself is a prime factor. 

The list of factors is then reconstructed to give a list of prime factors where each factor is listed the number of times it appears in the factorization. This is done by appended the number of times the divisor was repeated to the list of factors. The code then excludes 1, the number that was appended to the list, since it relates to the number of inverses that were taken and not to a prime factor.