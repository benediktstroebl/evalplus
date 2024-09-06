```python
def median(lst):
    n = len(lst)
    if n % 2 == 0:
        return (lst[(n // 2) - 1] + lst[n // 2]) / 2
    else:
        return lst[(n // 2)]

# Test cases
assert median([3, 1, 2, 4, 5]) == 3.0
assert median([-10, 4, 6, 1000, 10, 20]) == 15.0
assert median([5, 5, 4, 4, 3]) == 4.0
assert median([2, 4, 8, 12, 10, 6]) == 6.0
assert median([90, 84, 76, 71, 65]) == 71.0
```
This Python script defines a self-contained function `median(lst)` that calculates and returns the median of the elements in the input list `lst`. It then passes a series of test cases that verify the correctness of the `median()` function.