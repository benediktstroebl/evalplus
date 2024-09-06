```python
def factorize(n):
    """ Return list of prime factors of given integer in the order from smallest to largest
    """
    factors = []
    while n % 2 == 0:
        factors.append(2)
        n //= 2
    i = 3
    while i * i <= n:
        if n % i == 0:
            factors.append(i)
            n //= i
        i += 1
    for num in range(3, int(n**0.5) + 1, ]:
        if n % num == 0:
            factors.append(num)
            n //= num
    return factors
``` 
Do you have any other questions?