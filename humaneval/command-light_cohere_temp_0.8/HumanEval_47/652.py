```python
def median(lst):
    """Return the median of the list lst."""
    try:
        if len(lst) % 2 == 0:
            return (lst[len(lst) // 2 - 1] + lst[len(lst) // 2]) / 2
        else:
            return lst[len(lst) // 2]
    except IndexError:
        return "Input list is empty"

# Test the function
# We check if the list is empty first, so that we don't perform an index error
test_median = [10, 20, 40]
test_median.

assert median(test_median) == 15
```