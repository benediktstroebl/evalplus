```python
def factorize(n: int) -> List[int]:
    factors = []
    while n % 2 == 0:
        factors.append(2)
        n = n // 2
    for i in range(3, int(n**0.5) + 1,  while n % i == 0:
        factors.append(i)
        n = n // i
    return factors
``` 
This script defines a function factorize that takes an integer n as input and returns a list of prime factors of n, ordered from smallest to largest. It achieves this by checking divisibility from 2, then 3 up to the square root of n, and dividing n by each divisor until the number becomes a prime or smaller than the current divisor.