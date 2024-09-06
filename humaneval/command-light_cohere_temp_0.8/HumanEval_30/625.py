```python
def get_positive(lst):
    """Return only positive numbers in the list"""
    return [num for num in lst if num >= 0]

# Test the function with different lists of numbers

# Test with a list of all positive numbers
test_positive_list = [1, 2, 3, 4, 5]
assertEqual(get_positive(test_positive_list), [1, 2, 3, 4, 5])

# Test with a list of all negative numbers
test_negative_list = [-1, -2, -3, -4, -5]
assertEqual(get_positive(test_negative_list), [])

# Test with a list of mixed positive and negative numbers
test_mixed_list = [-5, 2, -3, 0, 6, -4]
assertEqual(get_positive(test_mixed_list), [2, 0, 6])

# Test with a empty list
test_empty_list = []
assertEqual(get_positive(test_empty_list), [])
``` 
This Python function `get_positive` takes a list as an argument and returns a new list containing only the positive numbers from the input list. 

The function uses list comprehension to iterate over each element in the input list and filter out the positive numbers using the condition `num >= 0`. 

This function is then used in various test cases to ensure its correctness and ability to handle different types of input lists.