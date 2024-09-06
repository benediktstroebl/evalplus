```python
def factorize(n: int) -> List[int]:
    factors = []
    while n % 2 == 0:
        factors.append(2)
        n //= 2
    for i in range(3, int(n**.5) + 1, step=4):
        while n % i == 0:
            factors.append(i)
            n //= i
    factors.append(int(n))
    return factors
```
The function returns a list of prime factors of the given integer, in order from smallest to largest. It uses a strategy of checking divisibility by powers of numbers until the square root of the input number.