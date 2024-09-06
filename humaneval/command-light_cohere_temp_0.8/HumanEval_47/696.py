```python
def median(l: list):
    """Return median of elements in the list l.
    if len(l) <= 1:
        return l[0]
    middle = len(l) // 2
    left = median(l[:middle])
    right = median(l[middle:])
    return (left + right) / 2

# Test cases
test_median = [
    [-10, 4, 6, 1000, 10, 20],
    [1, 2, 4, 5],
    [5, 5, 5, 5],
    [10, 20, 30, 40, 50]
]

for test in test_median:
    actual = median(test)
    assert actual == test[1], f"Wrong result for median: {test}"
```
The provided code defines a function called median that calculates the median of a given list. The function first checks if the list has less than two elements, in which case it returns the first element as the median. It then finds the specific about the middle element of the list, then calculates the median of the middle elements by finding the median of the elements before and after the middle element. Finally, it returns the result.