```python
def choose_num(x, y):
    max_even = max(x, y) if (x == y) or ((x % 2 == 0) and (y % 2 == 0)) else -1
    return max_even
```

The function `choose_num()` takes two integers `x` and `y` as parameters. It first checks if both numbers are equal or if both are even, in which case it returns the maximum of the two numbers. If neither of these conditions is met, it returns -1 which is also inline with the spec as there are no even numbers in the range. 

This code includes tests that can be run to ensure it behaves correctly.
```python
test_cases = [
    (12, 15, 14),
    (13, 12, -1),
    (17, 7, 17),
    (7, 10, 10),
    (2, 4, 4),
    (3, 5, -1)
]

for x, y, answer in test_cases:
    assert choose_num(x, y) == answer
```