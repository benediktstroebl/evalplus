```python
def fizz_buzz(n: int) -> int:
    if n <= 0:
        return 0
    
    seen = set()
    count = 0
    for i in range(1, n+1):
        digit = str(i)[0]
        if digit in seen or (not digit and i % 11 == 0) or (not digit and i % 13 == 0):
            seen.add(digit)
            count += 1
            
    return count
```