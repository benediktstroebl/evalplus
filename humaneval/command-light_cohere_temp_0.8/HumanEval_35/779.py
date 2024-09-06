```python
def max_element(lst):
    """Return maximum element in the list"""
    return max(lst)

# Test function to pass the test case
def test():
    lst = [5, 3, -5, 2, -3, 3, 9, 0, 123, 1, -10]
    assert max_element(lst) == 123

# Main function to call the test function with provided input
if __name__ == "__main__":
    test()
```