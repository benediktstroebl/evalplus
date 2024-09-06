```python
def max_element(lst):
    """Return maximum element in the list"""
    return max(lst)

#Test cases
def test():
    assert max_element([1, 2, 3]) == 3
    assert max_element([5, 3, -5, 2, -3, 3, 9, 0, 123, 1, -10]) == 123

# Main program
if __name__ == "__main__":
    test()
```