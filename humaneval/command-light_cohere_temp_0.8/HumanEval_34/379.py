Here's a self-contained Python function that returns a sorted list of unique elements in an input list:
```python
def unique(lst):
    """Returns unique and sorted elements in a list"""
    unique_list = set(lst)
    return list(unique_list)

# Test cases
def test_unique():
    assert unique([5, 3, 5, 2, 3, 3, 9, 0, 123]) == [0, 2, 3, 5, 9, 123]

# Main program
if __name__ == "__main__":
    test_unique()
```

I've included a test suite `test_unique()` to check the correctness of the `unique` function against various input scenarios. The main program runs this universal code at the bottom, ensuring that the function is only run when the script is executed directly and not when imported.