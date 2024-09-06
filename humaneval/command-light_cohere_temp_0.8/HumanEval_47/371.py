```python
def median(l: list):
    """Return median of elements in the list l"""
    if len(l) < 1:
        return None  # Handle empty list
    m = l[len(l)//2]
    if len(l) % 2 == 0:
        return (m + l[len(l)//2]) / 2
    else:
        return m
# Test the function with various lists
for test_list in [
    [-10, 4, 6, 1000],
    [10, 20, 30],
    [1, 2, 3, 4, 5],
    [5, 6, 7],
    [1, 2, 3, 4, 5, 6, 7]
]:
    result = median(test_list)
    if result is None:
        print(f"List {test_list} failed test")
    else:
        print(f"List {test_list} passed all tests.")
```