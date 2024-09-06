```python
def median(lst):
    """Return median of elements in the list lst"""
    n = len(lst)
    if n % 2 == 0:
        return (lst[n // 2 - 1] + lst[n // 2]) / 2
    else:
        return lst[n // 2]

# Test cases
test_median = [
    [float('-inf'), 4, 6, 1000, 10, 20],
    [3, 1, 2, 4, 5],
    [-10, 4, 6, 1000, 10, 20],
    [20, 10, 5, 3, 1],
]

for case in test_median:
    assert median(case) == case[1], f"Wrong median: {case}"
```
The function median takes a list and returns the median of the elements in that list. The median of a list of numbers is the value that is in the middle of the list. The function works by first, getting the length of the list, and then checking if the length of the list is even or odd. If the length of the list is even, the median is the average of the two middle numbers. If the length of the list is odd, the median is the middle number.