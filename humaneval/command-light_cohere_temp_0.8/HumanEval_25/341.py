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
This function identifies and returns the list of prime factors in order from the smallest to the largest, by dividing by each prime number starting from 2 and continuing until the number is no divisible by any prime.