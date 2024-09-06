```python
def largest_divisor(n: int) -> int:
    return next(i for i in range(1, n+1) if all(j % i == 0 for j in range(1, n+1)))
# tests
assert largest_divisor(1)==1
assert largest_divisor(6)==2
assert largest_divisor(9)==3
assert largest_divisor(15)==5
```