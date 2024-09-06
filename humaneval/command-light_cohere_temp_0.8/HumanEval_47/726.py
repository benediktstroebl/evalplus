```python
def median(l):
    """Return median of elements in the list l."""
    return (len(l) + 1) / 2 * (sum((x for x in l if x % 2 == 0)) + sum((x for x in l if x % 2 != 0)))
# Tests
    assert median([3, 1, 2, 4, 5]) == 3.0
    assert median([-10, 4, 6, 1000, 10, 20]) == 15.0
    assert median([1, 2, 3, 4, 5]) == 3.0
    assert median([10, 20, 30, 40, 1, 80]) == 15.0
``` 
This script defines a function median that computes the median of a list of numbers. The median is the average of the two middle numbers in the sorted list.