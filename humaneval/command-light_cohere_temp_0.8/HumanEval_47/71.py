```python
def median(l):
    # Sort the list
    l.sort(l)
    # Calculate the median from middle two elements
    median_ = l[(len(l) - 1) // 2]
    # If the list has an odd number of elements, return it
    if len(l) % 2 == 1:
        return median_
    # Return the average of the two middle numbers
    return (median_ + l[len(l) // 2]) / 2

# Test the function with a few examples
assert(median([3, 1, 2, 4, 5]) == 3)
assert(median([-10, 4, 6, 1000, 10, 20]) == 15.0)
```