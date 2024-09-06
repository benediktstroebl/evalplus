```python
def fizz_buzz(n: int):
    if n <= 0:
        return 0

    s = set()
    for d in range(1, n + 1):
        count = 0
        for i in range(1, n // d + 1):
            digit = d * i + 7
            if n % (d * i) == 0 and digit not in s:
                count += 1
        s.add(count)

    return s.size()
```