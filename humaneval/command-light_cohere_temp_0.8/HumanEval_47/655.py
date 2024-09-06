```python
def median(lst):
    """Return the median of the list lst."""
    if len(lst) % 2 == 0:
        return (lst[(len(lst) // 2) - 1] + lst[len(lst) // 2]) / 2
    else:
        return lst[len(lst) // 2]

# Test cases
test_median = [
    ([-10, 4, 6, 1000, 10, 20],),
    ([3, 1, 2, 4, 5],),
    ([-2000, -100, 0, 20],),
    ([10, -20, 30],),
    ([10, 20, 30],),
]

for test_case in test_median:
    assert median(test_case) == test_case[1], f"failed: {test_case}"

```
This Python script defines a function called `median` that computes the median of a list. It handles cases with odd and even numbers of elements, testing its functionality with various sample inputs.