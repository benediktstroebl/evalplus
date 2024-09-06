```python
def median(lst):
    """Return the median value of the list lst."""
    sorted_lst = sorted(lst)
    n = len(sorted_lst)

    # if n is even, return the mean of the two middle values
    if n % 2 == 0:
        return (sorted_lst[n//2 - 1] + sorted_lst[n//2]) / 2
    # if n is odd, return the middle value
    else:
        return sorted_lst[n//2]

# Test suite for the function
test_median = [
    ([-10, 4, 6, 1000, 10, 20], 15.0),
    ]
```

You can use this code with a markdown code block to define the function and test it as a whole: