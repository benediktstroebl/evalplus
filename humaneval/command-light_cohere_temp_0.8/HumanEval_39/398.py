```python
def prime_fib(n: int):
    if n <= 1:
        return n
    else:
        # Find the smallest prime factor
        spf = []
        while n % 2 == 0:
            spf.append(2)
            n //= 2
        for i in range(3, int(n ** 0.5) + 1, )):
            if n % i == 0:
                spf.append(i)
                n //= i
        for sp in spf:
            n = n // sp
        return n
```