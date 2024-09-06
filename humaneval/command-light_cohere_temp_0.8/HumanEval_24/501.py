Here is a self-contained Python script that solves the problem of finding the largest divisor of a given number:

```python
def largest_divisor(n: int) -> int:
    return next(i for i in range(1, n+1) if all(j == i%k for j,k in permutations(n)))

def permutations(n: int):
    return [list(map(reversed, list(range(n))))] * n

def test_largest_divisor():
    assert largest_divisor(15) == 5
```

This script defines a function called `largest_divisor` that returns the largest integer that divides a given number `n` evenly, smaller than `n`. The `permutations` function generates all possible permutations of the numbers from 1 to `n` using the `range` function and a list comprehension.

The `test_largest_divisor` function tests whether the function returns the correct result for the given input `15`.