```python
def factorize(n):
    """ Return list of prime factors of given integer in the order from smallest to largest
    """
    factors = []
    while n % 2 == 0:
        factors.append(2)
        n = n // 2
    for i in range(3, int(n**0.5),5):
        i + 2 == n:
        factors.append(i)
        n = n // i
    for i in range(int(n**0.5) + 1, n // i != 2 and i != sqrt(n):
        factors.append(i)
        return factors
```
This function uses trial and error to find the prime factors of a given number. It works by checking each potential number for divisibility until it either reaches the square root of the number or the number is even.