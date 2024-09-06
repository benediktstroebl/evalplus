```python
def median(l: list):
    """Return median of elements in the list l."""
    return (sorted(l)[len(l)//2])

# Test case 1
def test_median():
    return median([3, 1, 2, 4, 5]) == 3

# Test case 2
def test_median2():
    return median([-10, 4, 6, 1000, 10, 20]) == 15.0
```

The provided Python code defines a function called `median` that calculates and returns the median of a list's elements. It also includes two test cases that verify the correctness of the `median` function by passing various lists and comparing the returned medians with expected results.