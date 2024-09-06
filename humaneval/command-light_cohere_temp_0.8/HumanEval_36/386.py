```python
def fizz_buzz(n: int):
    if n <= 0:
        return 0
    count = 0
    for i in range(1, n+1):
        digit = str(i)[1]
        if digit == '7':
            count += 1
        if i % 11 == 0 or i % 13 == 0:
            count += 1
    return count
```