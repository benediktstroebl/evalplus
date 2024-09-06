```python
from typing import List
def factorize(n: int) -> List[int]:
    factors = []
    while n % 2 == 0:
        factors.append(2)
        n //= 2
    for i in range(3, int(n**0.5) + 1, while n % i == 0:
        factors.append(i)
        n //= i
    factors.append(n)
    return factors
```
The function factorize takes an integer n as input and returns a list of its prime factors. The function first checks if n is divisible by 2, and if so, appends 2 to the list of factors. Then, it iterates through the range of prime numbers (3 to n**5), and checks if n is divisible by each prime number. If a number is found, append it to the list of factors. 

Finally, the function appends the original n to the list of factors, which is the list of prime factors of the number n, ordered from smallest to largest.