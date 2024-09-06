```python
def factorize(n: int) -> List[int]:
    factors = []
    while n % 2 == 0:
        factors.append(2)
        n = n // 2
    for i in range(3, int(n ** 0.5) + 1, )):
        while n % i == 0:
            factors.append(i)
            n = n // i
    if n > 2:
        factors.append(n)
    return factors
```
The function factorizes an integer n by finding its prime factors. It starts by checking if n is divisible by 2. If it is, it adds 2 to the list of factors. Then, it checks for larger prime factors, starting from 3 up. It continues this process until the pattern until no more divisors are found.