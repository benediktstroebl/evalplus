```python
def median(lst):
    """Return median of elements in the list lst"""
    if len(lst) < 1:
        raise ValueError("Input list is empty")
    if len(lst) == 1:
        return lst[0]
    med = []
    for i in range(0, len(lst), 2):
        med.append(lst[i])
    return (1.0 / 2) * med[0] + (len(med) - 1) * med[1])

# Test the function with a variety of cases
if median([3, 1, 2, 4, 5]) != 3:
    raise Exception("Function does not return expected result")
if median([-10, 4, 6, 1000, 10, 20]) != 15:
    raise Exception("Function does not return expected result")
if median([1, 2, -5]) != 2:
    raise Exception("Function does not return expected result")
```