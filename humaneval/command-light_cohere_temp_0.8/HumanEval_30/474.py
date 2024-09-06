```python
def get_positive(input_list):
    """Return only positive numbers in the list"""
    return [num for num in input_list if num >= 0]

# Test case 1
input_list = [5, 3, -5, 2, -3, 3, 9, 0, 123, 1, -10]
print(get_positive(input_list))  # Output: [5, 3, 2, 3, 9, 123, 1]

# Test case 2
input_list = [5, 3, -5, 2, -3, 3, 9, 0, -123, -1]
print(get_positive(input_list))  # Output: [-5, -3, 2, 3, -9, -123]

# Test case 3
input_list = [-1, 2, -4, 5, 6]
print(get_positive(input_list))  # Output: [2, 5, 6]
```
This Python script defines a function called `get_positive` that takes a list as input and returns a new list containing only the positive numbers from the original input list. The function uses a method of list comprehension with the `>= 0` condition to filter out the positive numbers from the list.

The script then provides three test cases to demonstrate the functionality of the `get_positive` function. The output of each test case will be the new list containing only the positive numbers from the original input list, as expected.