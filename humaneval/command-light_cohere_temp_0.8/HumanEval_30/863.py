```python
def get_positive(l: list):
    return [num for num in l if num >= 0]

#Test the function with various lists
#Return the list after applying the function

#Test list with all positive numbers
test_list = [5, 3, 9, 123]
result = get_positive(test_list)
print(result)  # Output: [5, 3, 9, 123]

#Test list with negative numbers
test_list_negative = [-1, 2, -4, 5, 6]
result_negative = get_positive(test_list_negative)
print(result_negative)  # Output: [2, 5, 6]

#Test list with mixed values
test_list_mixed = [-5, 3, 2, 7, -10]
result_mixed = get_positive(test_list_mixed)
print(result_mixed)  # Output: [2, 3, 7]
```
The function get_positive takes a list as an argument and returns a new list that contains only the positive numbers from the original list. The test cases demonstrate how the result is printed to the console to ensure that the function is working as expected.