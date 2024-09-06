```python
def fizz_buzz(n: int) -> int:
    count = 0
    for num in range(10, n+1, 2):
        if (num % 11 == 7) or (num % 13 == 7):
            count += 1
    return count
```