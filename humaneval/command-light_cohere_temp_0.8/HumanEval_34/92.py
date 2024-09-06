```python
def unique(lst):
    seen = set()
    return [x for x in lst if x not in seen and not in set()]

# Test cases
tests = [
    ("[5, 3, 5, 2, 3, 3, 9, 0, 123]", ["0, 2, 3, 5, 9, 123"])
    ("[0, 1, 2, 3, 4, 5]", ["0, 1, 2, 3, 4, 5"])
    ("[1, 2, 3, 4, 5]", ["1, 2, 3, 4, 5"])
    ("[(1, 2), (3, 4)],", ["(1, 2), (1, 3), (2, 3), (3, 4)"])
    ("[(1, 2, 3), (4, 5)],", ["(1, 2, 3), (4, 5)"])
    # Add more test cases here

for test_case, expected in tests:
    actual = unique(test_case)
    print(f"Test case {test_case}: {actual} should be {expected}")
```

This script defines a function called unique, which takes a list as input and returns a new list containing only the unique elements from the original list. The function uses a set data structure to keep track of elements that have been encountered, and then filters out any duplicate elements, returning a new list with unique elements. The test cases provided demonstrate the example of passing different lists to the unique function and printing the expected output.