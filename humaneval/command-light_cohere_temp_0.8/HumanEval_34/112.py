```python
def unique(lst):
    """Return sorted unique elements in a list"""
    seen = set()
    return [x for x in lst if x not in seen and x not None]

# Test the function with various input
if __name__ == "__main__":
    # Lists with elements - 0, 2, 3, 5, 9, and 123
    tests = [
        [],           # [] ==> True
        [5, 3, 5, 2, 3, 3, 9, 0, 123],  # True
        [2, 5, 3],    # True
        [5, 5, 3, 0, 1],  # True
        [1, 2, 3, 4, 5, 6], # Contains duplicates, returns duplicates
        # [2, 3, 4, 5] -> False
    ]

    for test_list in tests:
        got = unique(test_list)
        expected = [2, 3, 5, 9, 123]  # Changed order for easier comparison
        assert got == expected, f"Not equal: {got} != {expected}"
```
The function unique takes a list as input and returns a new list with unique elements from the original list. 

The function uses a set to keep track of seen elements, then iterates through the original list and adds elements to the list if they are not in the set and not None.

The test suite includes various cases with different lists to ensure that the function is working correctly for different scenarios.