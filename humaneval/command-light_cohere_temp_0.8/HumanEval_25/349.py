```python
def factorize(n: int) -> List[int]:
    factors = []
    while n % 2 == 0:
        factors.append(2)
        n = n // 2
    for i in range(3, int(n**0.5) + 1, while n % i == 0:
        factors.append(i)
        n = n // i
    for i in range(int(n**0.5) + 2, n % i != 0:
        factors.append(i)
    return factors
```
This function, factorize, takes an integer n as input and returns a list of its prime factors. It uses a list comprehension and the `islic` function to identify all prime factors of n, and the order in which they are returned is the order of smallest to largest prime factors.