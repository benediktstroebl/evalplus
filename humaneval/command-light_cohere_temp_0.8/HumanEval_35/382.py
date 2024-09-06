```python
def max_element(lst):
    """Return maximum element in the list."""
    return max(lst)

# Test function
def test_max_element():
    try:
        print(max_element([5, 3, -5, 2, -3, 3, 9, 0, 123, 1, -10]))
    print("Passed test!")

# Call test function
test_max_element()
```