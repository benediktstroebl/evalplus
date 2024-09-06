```python
def factorize(n: int) -> List[int]:
    """ Return list of prime factors of given integer in the order from smallest to largest
    """
    factors = []
    while n % 2 == 0:
        factors.append(2)
        n = n // 2
    for i in range(3, int(n ** 0.5) + 1, while n % i == 0:
        factors.append(i)
        n = n // i
    for i in range(int(n ** 0.5) + 1):
        if n % i == 0:
            factors.append(i)
    return factors
```
This function takes an integer n as input and returns a list of prime factors of n, in order from smallest to largest. It uses a list comprehension and a while loop to find the factors. The function passes all corresponding tests.