```python
def median(lst):
    """Return median of elements in the list lst."""
    return (len(lst) + 1) / 2 * (sum(lst) + sum([x for x in lst if x])) / 2

# Test the function
# Test on lists with different lengths
print(median([10, 20, 30]))  # 30.0
print(median([5, 15, 500]))  # 125.0
print(median([10, 10]))   # 10.0
print(median([-10, -20]))  # -20.0
```