Here's the solution:
```python
def fizz_buzz(n: int) -> int:
    counts = 0
    for num in range(2, n+1):
        d = 0
        while num % 11 == 0 or num % 13 == 0:
            d += 1
        counts += d
    return counts
```