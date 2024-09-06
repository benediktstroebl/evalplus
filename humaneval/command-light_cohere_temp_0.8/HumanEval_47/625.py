```python
def median(lst):
    n = len(lst) // 2 + 1
    m1, m2 = n // 2, n // 2 + 1
    median_value = (lst[m1] + lst[m2]) / 2
    return median_value

# Test the function with a few examples
test_median = lambda: median([3, 1, 2, 4, 5]) == 3 and median([10, 4, 6, 1000, -10, 20]) == 15.0
```

The function median takes a list `lst` as input and returns the median value of its elements. It calculates the two indices of the middle elements (the first and the last) using integer division of the length of the list. Then, it calculates the median value as the average of these middle elements.