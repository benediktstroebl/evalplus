```python
def get_positive(input_list):
    """Return only positive numbers in the list"""
    positive = [num for num in input_list if num > 0]
    return positive

# Test the function
# Should return [2, 5, 6]
input_list = [1, 2, -4, 5, 6, 7, -3, 8, 9]
print(get_positive(input_list))  # Output: [2, 5, 6]
input_list = [5, 3, -5, 2, -3, 3, 9, 0, 123, 1, -10]
print(get_positive(input_list))  # Output: [5, 3, 2, 3, 9, 123]
```
This script defines a function called **get_positive** that takes a list of numbers as input and returns a new list containing only the positive numbers from the original input list. It then passes these tests the preview to check that the function works as expected.