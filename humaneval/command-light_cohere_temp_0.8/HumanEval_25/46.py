```python
def factorize(n: int) -> List[int]:
    factors = []
    while n % 2 == 0:
        factors.append(2)
        n = n // 2
    for i in range(3, int(n**0.5) + 1,):
        while n % i == 0:
            factors.append(i)
            n = n // i
    if n > 2:
        factors.append(n)
    return factors
```

This Python function, `factorize`, takes an integer `n` as input and returns a list of its prime factors. The function uses a iterative approach to find the prime factors, starting with the assumption that 2 is a factor. The function then iterates through numbers from 3 up, checking for divisibility, and when a number is divisible by a given number, it's added to the list of prime factors. The function then returns the list of prime factors of the original number.