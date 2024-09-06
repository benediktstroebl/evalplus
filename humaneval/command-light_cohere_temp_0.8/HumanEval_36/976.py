```python
def fizz_buzz(n: int):
    c = 0
    for i in range(1, n+1):
        digit = str(i)[0]
        while digit == '7' and i % 11 == 0 or i % 13 == 0:
            digit = str(i)[0] = digit
        c += 1
    return c
```