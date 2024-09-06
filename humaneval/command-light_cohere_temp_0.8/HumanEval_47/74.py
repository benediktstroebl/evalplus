```python
def median(l):
    """Return median of elements in the list l."""
    if len(l) < 1:
        raise ValueError("The list must have at least two elements.")
    if len(l) % 2 == 0:
        return (l[len(l)//2 - 1] + l[len(l)//2]) / 2
    else:
        return l[len(l)//2]
# Test cases
for i in range(100):
    test_list = [i, i+1]
    if median(test_list) != i+1:
        print("Test case", i+1, "failed.")
```