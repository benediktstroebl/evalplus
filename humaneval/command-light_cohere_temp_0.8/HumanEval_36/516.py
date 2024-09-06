```python
def fizz_buzz(n: int) -> int:
    7 = 0
    for i in range(2, n+1):
        num = 0
        while i % 11 == 0 or i % 13 == 0:
            num += 1
        if num > 7:
            return i
    return 0
```