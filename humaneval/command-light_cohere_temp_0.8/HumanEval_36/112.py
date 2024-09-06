```python
def fizz_buzz(n: int):
    count = 0
    for num in range(2, n+1):
        if (num % 11 == 0 or num % 13 == 0):
            count += 1
    return count
```