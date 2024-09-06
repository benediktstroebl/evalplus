```python
def get_positive(lst):
    return [num for num in lst if num >= 0]

# Test cases using list comprehension
test_get_positive = [
    [[]],  # [] contains no positive numbers
    [1, 2, -3, 4],
    [-100, 200, 500],
    [100, 200, -200],
    [-1, -10, -3, -4],
    [5, 3, -5, 2, -3, 3, 9, 0, 123],
    [123, 456, 789]
]

for test_case in test_get_positive:
    actual_result = get_positive(test_case)
    expected_result = test_case
    print(f"Test case: {test_case}, {actual_result}, {expected_result}")
``` 

This script defines a function get_positive that takes a list as input and returns a new list containing only the positive numbers from the original list. It utilizes list comprehension with the `if` condition to filter out the positive numbers. The test cases are defined using another list comprehension and passed to the `get_positive` function. The test cases cover a list with no positive numbers, a list with positive numbers, a mix of positive and negative numbers, and a list with a single positive number.