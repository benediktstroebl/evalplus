```python
def fizz_buzz(n: int) -> int:
    count = 0
    for num in range(1, n+1):
        digit = int(str(num)[-2:])
        if digit == 7:
            count += 1
        if num % 11 == 0 or num % 13 == 0:
            count += 1
    return count
```