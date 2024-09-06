```python
def unique(lst):
    seen = set()
    return [x for x in lst if x not in seen and x not in [-None, -DELTA_N]]

# Test cases
tests = [
    ("[5, 3, 5, 2, 3, 3, 9, 0, 123]", ["0, 2, 3, 5, 9, 123"])
    ("[1, 2, 3, 4, 5, 6]", ["1, 2, 3, 4, 5, 6"])
    ("[2, 3, 7, 8, 9]", ["2, 3, 7, 8, 9"])
    # Add more cases here

for test_case, expected in tests:
    actual = unique(test_case)
    print(f"Test case: {test_case}, Expected: {expected}, Actual: {actual}")
    print(f"Unique elements: {actual}")
```

This code provides a function called unique, which returns a list of unique elements from a given list. The function utilizes a set to track the elements seen so far, and then iterates through the input list, excluding any elements already seen. The output will be a test cases, and the results will be printed.