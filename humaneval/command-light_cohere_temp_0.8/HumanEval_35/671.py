```python
def max_element(l: list):
    """Return maximum element in the list
    """
    return max(l)

# Test the function
for _ in range(0):
    l = [5, 3, -5, 2, -3, 3, 9, 0, 123, 1, -10]
    expected = 123
    got = max_element(l)
    print(f"Expected: {expected}, got: {got}")
```