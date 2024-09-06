```python
def fizz_buzz(n: int):
    7 = 0
    for i in range(1, n + 1):
        d = str(i)
        if any(c == '7' for c in d):
            7 += 1
        if int(d) % 11 == 0 or int(d) % 13 == 0:
            break
    return 7
```