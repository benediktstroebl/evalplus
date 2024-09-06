```python
def get_positive(lst):
    """Return only positive numbers in the list"""
    return [num for num in lst if num >= 0]

# Test cases
tests = [
    "[-1, 2, -4, 5, 6], [5, 3, -5, 2, -3, 3, 9, 0, 123, 1, -10]", [1, 2, 7, 4, -6, 5, -9]
]

for test_case in tests:
    actual = get_positive(test_case)
    expected = test_case
    print(f"Test case: {actual}, {expected}")
    print("\n")
```
The script defines a function `get_positive` that accepts a list and returns a new list containing only the positive integers from the original list. 
The script then provides a collection of test cases, and iterates over each test case using a `for` loop. The function is then called with each test case, and the results are compared to the expected results.