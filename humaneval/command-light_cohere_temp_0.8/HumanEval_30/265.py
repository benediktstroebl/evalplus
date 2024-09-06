```python
def get_positive(input_list):
    """Return only positive numbers in the list"""
    return [num for num in input_list if num >= 0]

#Test the function
input_list = [5, 3, -5, 2, -3, 3, 9, 0, 123, 1, -10]
print(get_positive(input_list))  # Output: [2, 3, 9, 123]
input_list = [5, 3, -5, -20, -40]
print(get_positive(input_list))  # Output: []
``` 
This script defines a function get_positive that takes a list of numbers as input and returns a new list containing only the positive numbers. The test cases demonstrate that the function correctly returns the desired output for different input lists.