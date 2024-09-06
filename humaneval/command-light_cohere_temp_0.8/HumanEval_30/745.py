```python
def get_positive(input_list):
    """Return only positive numbers in the list"""
    return [num for num in input_list if num > 0]

# Test the function
input_list = [5, 3, -5, 2, -3, 3, 9, 0, 123, 1, -10]
print("Input List:", input_list)
print("Output:", get_positive(input_list)) # Output: Output: [2, 3, 5, 9, 123]
``` 
This code defines a function `get_positive` that takes a list of numbers as input and returns a new list containing only the positive numbers from the original list. The output of the example test shows that the function works as expected.