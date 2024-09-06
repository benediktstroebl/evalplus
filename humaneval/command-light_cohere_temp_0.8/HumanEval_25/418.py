```python
def factorize(n: int) -> List[int]:
    factors = []
    while n % 2 == 0:
        factors.append(2)
        n = n // 2
    for i in range(3, int(n**0.5) + 1, while n % i == 0:
        factors.append(i)
        n = n // i
    factors.append(n)
    return factors
```
The function factorizes a given number n and returns a list of its prime factors in order from the smallest to the largest. Each factor is listed number of times corresponding to how many times it appears in factorization.

This function is self-contained and provides a solution for the problem of finding prime factors of a given number.