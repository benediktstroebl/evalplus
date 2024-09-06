Here is a self-contained Python script that defines a function to find the largest divisor of a given number:

```python
def largest_divisor(n: int) -> int:
    """ Returns the largest divisor of the given number n.
    if n <= 1:
        return n
    # prime factorization
    d = n - 1
    while d % 2 == 0:
        n -= 1
        d //= 2
    for i in range(3, int(n ** 0.5) + 1, steps(i):
        factors = [i]
        while n % i == 0:
            factors.append(n // i * i) // j for j <= i
            n //= i
        if n <= 1:
            return n
        return max(factors)
```