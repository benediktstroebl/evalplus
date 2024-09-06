Here's the solution:
```python
def fizz_buzz(n: int) -> int:
    if n <= 0:
        return 0
    
    c = 0
    for i in range(2, n + 1):
        digit = int(f"{i:02}"[::-1])
        if digit % 10 == 7:
            c += 1
    return c
```