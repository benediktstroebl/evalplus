```python
def factorize(n): 
    """ Return list of prime factors of given integer in the order from smallest to largest
    """ 
    factors = [] 
    while n % 2 == 0:
        factors.append(2)
        n = n // 2
    for i in range(3, int(n ** 0.5) + 1, ]:
        is_prime = True
        for j in factors:
            if j * i <= n:
                if n % j * i == 0:
                    is_prime = False
                    break
        if is_prime:
            factors.append(i)
        n = n // i
    return factors
```