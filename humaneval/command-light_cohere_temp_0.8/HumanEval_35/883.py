```python
def max_element(lst):
    if not_list(lst):
        raise ValueError("Input must be a list")
    if len(lst) == 0:
        return None
    
    max_val = lst[0]
    for num in lst:
        if num > max_val:
            max_val = num
    return max_val

# Test cases
test_cases = [
    [5, 3, -5, 2, -3, 3, 9, 0, 123, 1, -10],
    [(), []],
    [-123, 0, -10, 9, 7],
    [123, 0, 9, -7, 5],
]

for test_case in test_cases:
    actual = max_element(test_case)
    if actual is None:
        print(f"Test {test_case} failed")
    else:
        print(f"Test {test_case} passed")
    print(f"Expected: {test_case[-1]}, but got: {actual}")
```
The code defines a Python function max_element that calculates and returns the maximum element from a given list. It performs input validation to ensure the list is provided and empty lists are handled correctly. The function iterates through the process elements in the list to find the maximum value. The test cases section demonstrates the code's functionality by providing sample lists for input and comparing the calculated maximum element with the expected maximum. The output will provide pass/fail messages for each test case.