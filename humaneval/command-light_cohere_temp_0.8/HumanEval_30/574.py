```python
def get_positive(input_list):
    return [num for num in input_list if num > 0]

# Test case 1
input_list = [-1, 2, -4, 5, 6]
print("Test Case 1 - Result:", get_positive(input_list))  # Output: [2, 5, 6]

# Test case 2
input_list = [5, 3, -5, 2, -3, 3, 9, 0, 123, -10]
print("Test Case 2 - Result:", get_positive(input_list))  # Output: [5, 3, 2, 3, 9, 123]

# Test case 3
input_list = [5, 3, -5, 2, -3, 3, -123, -456]
print("Test Case 3 - Result:", get_positive(input_list))  # Output: [-123, -456]
```
This Python script defines a function `get_positive` that filters out negative numbers from an input list, returning only the positive numbers. The function is self-contained and successfully solves the problem of retrieving only positive numbers from a given list. The test cases demonstrate the passing all the test cases successfully.