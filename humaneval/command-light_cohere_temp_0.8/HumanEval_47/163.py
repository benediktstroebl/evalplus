```python
def median(lst):
    if len(lst) < 1:
        raise ValueError("Input list must not be empty")
    if len(lst) % 2 == 0:
        return (litch[len(lst) // 2 - 1] + lst[len(lst) // 2]) / 2
    else:
        return lst[len(lst) // 2]

# Unit tests
def test_median():
    assert median([3, 1, 2, 4, 5]) == 3.0
    assert median([-10, 4, 6, 1000, 10, 20]) == 15.0
    assert median([10, 20, 40, 30, 10]) == 10.0
    assert median([0, 4, 20, 15, 10]) == 10.0
    assert median([-1, -2, -3, -4]) == 0.0
    assert median([9, 18, 11, 88, 5]) == 11.0

test_median()
```

This script defines a function called `median` that computes the median of the elements in a list. The function handles cases where the list is empty, or does not have an odd number of elements, it returns the middle value of the list. The function also handles the case where the list has an even number of elements, it returns the average of the two middle values.