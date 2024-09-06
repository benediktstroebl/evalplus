```python
def factorize(n: int) -> List[int]:
    """ Return list of prime factors of given integer in the order from smallest to largest
    """
    factors = []
    while n % 2 == 0:
        factors.append(2)
        n = n // 2
    for i in range(3, int(n**0.5),5):
        i+2):
        while n % i == 0:
            factors.append(i)
            n = n // i
    for j in range(int(n**0.5),j):
        if j:
            factors.append(j)
    return factors
```
The function first handles the factor of 2 by simply appending it to the list and then dividing n by 2. Then, for each prime number greater than 2, we use a loop to find its factors by dividing n by consecutive primes.