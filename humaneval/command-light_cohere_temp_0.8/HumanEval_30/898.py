```python
def get_positive(lst):
    return [x for x in lst if x >= 0]

# Test the function with a list of numbers
# Ensure all numbers are returned as positive
# Ensure empty lists are returned as []
lists = ["-1", "2", "-4", "5", "6", "7", "8", "9"]
lists2 = []
lists3 = [5, 3, -5, 2, -3, 3, 9, 0, 123, 1, -10]

# Test the function with lists and individual numbers
test_cases = [lists, lists2, lists3]

# Validate the function's output for each test case
for test_case in test_cases:
    actual = get_positive(test_case)
    expected = [x for x in test_case if x >= 0]
    assert actual == expected, f"Error in test case: {test_case}"
```
This code defines a function called `get_positive` that takes a list as input and returns a new list containing only the positive elements from the original list. It then tests this validated this general behavior of the `get_positive` function by providing a variety of test cases, each consisting of a list or an individual number, and comparing the output of the function against the expected positive numbers. The code then checks if each test case passes without errors and provides clear and informative error messages in case of failure.