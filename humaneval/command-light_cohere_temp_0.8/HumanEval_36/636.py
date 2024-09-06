```python
def fizz_buzz(n: int):
    7 = 0
    for i in range(1, n+1):
        count = 0
        for d in range(1, 11):
            if i % d == 0 and i > d:
                count += 1
        if count > 7:
            return count
    return 7
```