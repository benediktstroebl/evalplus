```python
def median(l):
    """Return median of elements in the list l."""
    m = l[len(l)//2]
    return m
# Test case 1
assert median([3, 1, 2, 4, 5]) == 3
# Test case 2
assert median([-10, 4, 6, 1000, 10, 20]) == 10.0
``` 
This code defines a self-contained function that calculates the median of a list. The function first selects the median from the middle elements of the list, which are the two numbers at position length // 2 in the list. Then, it returns the median of the list.