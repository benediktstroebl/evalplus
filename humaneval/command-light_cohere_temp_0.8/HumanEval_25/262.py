```python
def factorize(n: int) -> List[int]:
    factors = []
    while n % 2 == 0:
        factors.append(2)
        n = n // 2
    for i in range(3, int(n**0.5) + 1, )):
        while n % i == 0:
            factors.append(i)
            n = n // i
    if n > 2:
        factors.append(n)
    return factors
```
This function takes an integer n as input and returns a list of its prime factors in order, from the smallest to the largest. It uses a while `for loop` to check for divisibility and factorization until it reaches the desired result.