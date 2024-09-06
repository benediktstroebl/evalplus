```python
def median(l: list):
    """Return median of elements in the list l."""
    try:
        med = [x for x in l if x % 2 == 0][0] + [x for x in l[::-1] if x % 2 == 1][0] / 2
        return med
    except IndexError:
        raise ValueError("Input list is empty")

# Test the function
# Test with empty list
test_median([]);
# Test with one element
test_median([10])
# Test with two identical elements
test_median([10, 10])
# Test with sorted list
test_median([1, 2, 3, 4, 5])
# Test with list of negatives
test_median([-10, 4, 6, 1000, 10, 20])
```