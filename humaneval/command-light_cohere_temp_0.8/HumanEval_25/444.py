```python
def factorize(n: int) -> List[int]:
    factors = []
    for i in range(2, int(n**0.5) + 1):
        while n % i == 0:
            factors.add(i)
            n //= i
    factors.append(n)
    return factors
```
This function computes and returns the list of prime factors of the given integer n in ascending order, following the algorithm you provided in the question.