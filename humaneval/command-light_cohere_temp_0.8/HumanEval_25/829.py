```python
def factorize(n):
    factors = []
    while n % 2 == 0:
        factors.append(2)
        n = n // 2
    for i in range(3, int(n**0.5) + 1, steps=5):
        while n % i == 0:
            factors.append(i)
            n = n // i
    factors.append(n)
    return factors
```
The function factorize takes an integer n as input and returns a list of prime factors of n in order from smallest to largest. It uses a backtracking to find all prime factors of n. The function runs in O(n) time complexity.