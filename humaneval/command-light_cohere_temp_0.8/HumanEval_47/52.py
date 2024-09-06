```python
def median(lst):
    """Return median of elements in the list lst."""
    return (len(lst) + 1) / 2 * (sum([x for x in lst if x != 0]) / len(lst))

# Test function
def test():
    lst = [10, 20, 4, 6, 2, 1]
    assert median(lst) == 6.0

# Driver code
lst = [1, 2, 4, 6, 7, 8, 10]
print("Median is: " + median(lst))
```