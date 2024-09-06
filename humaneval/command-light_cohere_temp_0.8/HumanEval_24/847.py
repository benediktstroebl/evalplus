```python
def largest_divisor(n: int) -> int:
    return next(i for i in range(1, n+1) if any(n%i == 0))
```
The provided code defines a Python function `largest_divisor` that efficiently finds the largest divisor of a given integer `n`. 

It achieves this by using a generator expression with the `range` function and the any() function. 

It iterates from 1 to `n` inclusive, and for each iteration checks if any of the residues ( remainders by division) of `i` with `n` are equal to 0. 

The first occurrence of such is returned.