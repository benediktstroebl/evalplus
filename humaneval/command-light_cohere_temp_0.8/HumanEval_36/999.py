```python
def fizz_buzz(n: int) -> int:
    seen = set()
    for num in range(1, n+1):
        if num % 11 == 7 or num % 13 == 7:
            seen.add(num)
    if seen == set(['7']):
            return num + 1
    return 0
```