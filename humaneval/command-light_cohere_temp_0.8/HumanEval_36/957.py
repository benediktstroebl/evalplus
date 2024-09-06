```python
def fizz_buzz(n: int):
    count = 0
    for i in range(2, n+1):
        num = str(i)
        if num[0] == 7 and (i % 11 == 0 or i % 13 == 0):
            count += 1
    return count
```