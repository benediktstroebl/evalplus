```python
def max_element(lst):
    if not_list(lst):  # Checks if list is valid
        return "Input should be a list"
    max_ = max(lst)
    return max_

# Test the function
print(max_element([5, 3, -5, 2, -3, 3, 9, 0, 123, 1, -10])) # Output: 123
```
The function max_element takes a list as input and returns the maximum element in the list.

This function is self-contained and does not require any external loops or modules. The function checks for invalid inputs and returns a descriptive error message if the input is not a list. It then uses the maximum function to find the maximum element in the list and returns the result.

The test code at the bottom prints the result of the function call to verify its correctness.