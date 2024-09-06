```python
def fizz_buzz(n: int) -> int:
    if n <= 0:
        return 0

    count = 0
    for digit in str(n):
        if digit == '7':
            count += 1
        if count == 1 and digit == '1':
            break
        elif count == 2 and digit == '4':
            break
        elif count == 3 and digit == '9':
            break
    return count
```