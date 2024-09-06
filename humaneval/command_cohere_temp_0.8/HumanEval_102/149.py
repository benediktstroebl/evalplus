```python
def choose_num(x, y):
    max_even = max((z for z in range(x, y + 1) if z % 2 == 0), default = -1)
    return max_even
```

The code defines a function choose_num that takes two positive numbers x and y, which returns the largest even integer within the range [x, y] inclusive. If there is no such number in the range, it returns -1. The function employs generator expression (z for z in range(x, y + 1) if z % 2 == 0) to yield all even numbers in the range. The max function with default parameter -1 returns the largest even number, or -1 if no even numbers are found.

Here is a simple test to ensure the function is working as expected:
```python
assert choose_num(12, 15) == 14
assert choose_num(13, 12) == -1
``` 

This test verifies that the function correctly identifies the largest even number in the range [12, 15] as 14 and that it also identifies the absence of even numbers in the range [13, 12].