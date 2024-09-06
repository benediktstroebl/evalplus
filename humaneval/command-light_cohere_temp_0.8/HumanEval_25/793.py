```python
def factorize(n):
    """ Return list of prime factors of given integer in the order from smallest to largest.
    """
   
    if n <= 1:
        return []
    elif n <= 3:
        return [n]
    else:
        factors = []
        while n % 2 == 0:
            n = n // 2
            factors.append(2)
        while n % 3 == 0:
            n = n // 3
            factors.append(3)
        while n % 5 == 0:
            n = n // 5
            factors.append(5)
        for i in range(6, int(n**(0.5) + 1) + 1):
            factors.append(i)
        return factors
```

This function uses basic prime factorization logic. It starts by checking if the number is less than or equal to 1. Then, it handles numbers <= 3, returning them directly. For bigger numbers, it creates a list of factors, initially starting with the square of the number and adding the corresponding prime factors, up to the square root of the original number.