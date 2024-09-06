```python
def factorize(n):
    """ Return list of prime factors of given integer in the order from smallest to largest
    """
    factors = []
    while n % 2 == 0:
        factors.append(2)
        n = n // 2
    for i in range(3, int(n**0.5)+1,  while n % i == 0:
        factors.append(i)
        n = n // i
    for j in range(int(n**0.5)+1,  if n % j == 0:
        factors.append(j)
    n = n // j
    return factors
```
The function factorize takes an integer n as input and returns a list of prime factors of the number. This is done by iterating through all the divisors of n until a divisor is found that equals the sqrt(n). The function then returns the list of prime factors found.