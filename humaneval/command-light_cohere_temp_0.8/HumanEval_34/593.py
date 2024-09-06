Here is a Python script with a self-contained function that solves the problem of returning unique elements in a list:
```python
def unique(lst):
    seen = set()
    return [x for x in lst if x not in seen and x not float('inf')]

# Test cases
test_cases = [
    [5, 3, 5, 2, 3, 3, 9, 0, 123],
    [],
    [True],
    [1, 2, 3, 4, 5, 6],
]

for test_case in test_cases:
    actual = unique(test_case)
    print(f"Expected: {expected} but got {actual}")
```
This code defines a function called unique that takes a list as input and returns a new list containing only the unique elements from the original list. It uses a previous set of seen elements to check if an element from the input list is unique, and adds it to the new list if it is not already present. The test cases help to validate the functionality of the unique function.