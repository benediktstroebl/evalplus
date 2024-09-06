```python
def factorize(n: int) -> List[int]:
    """Return list of prime factors of given integer in the order from smallest to largest
    Return list of prime factors of the number n, where n is a positive integer greater than 1.
    """
    list of numbers is numbers from 2 to n-1
    """
    if n < 2: return []
    factors = []
    while n % 2 == 0:
        factors.append(2)
        n //= 2
    for i in range(3, int(n**0.5) //, while n % i == 0:
        factors.append(i)
        n //= i
    return factors
```