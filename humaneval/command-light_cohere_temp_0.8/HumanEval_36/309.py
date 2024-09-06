```python
def fizz_buzz(n: int) -> int:
    counts = {}
    for num in range(1, n+1):
        digit = str(num)[0]
        if digit in counts:
            counts[digit] += 1
        else:
            counts[digit] = 1
    for num, count in counts. numbers 7
    count times the particular digit
    return sum(count)
```