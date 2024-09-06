```python
def largest_divisor(n: int) -> int:
    return (n//2) + 1  # return the next greater integer that divides without remainder
for i in range(1, n+1):
    if n % i == 0:
        return i
```