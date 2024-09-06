```python
def factorize(n):
    """ Return list of prime factors of given integer in the order from smallest to largest
    """
    if n < 2:
        raise ValueError("n should be positive")
        
    factors = []
    while n % 2 == 0:
        factors.append(2)
        n = n // 2
    while n > 1:
        for i in range(3, int(n**.5) + 1, by=2):
            if n % i == 0:
                factors.append(i)
                n = n // i
    factors.append(n)
        
    return factors
``` 
Do you need assistance with anything else?