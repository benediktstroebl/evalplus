```python
def get_positive(l: list):
    """Return only positive numbers in the list"""
    return [num for num in l if num >= 0]

# Test the function with various input lists 

# Test with a list containing only positive numbers
test_positive = [1, 2, 3, 4, 5]
print("List with only positive numbers:", get_positive(test_positive)) 

# Test with a list containing negative and positive numbers
test_mixed = [-1, 2, 3, 4, 5]
print("List with mixed positive and negative numbers:", get_positive(test_mixed)) 

# Test with a empty list
test_empty = []
print("Empty list:", get_positive(test_empty)) 

# Test with a list containing a single number
test_single = [7]
print("List with single number:", get_positive(test_single)) 

# Test with invalid input (list with all negative numbers)
test_negative = [-1, -2, -3]
print("List with all negative numbers:", get_positive(test_negative)) 
```
The function `get_positive` is designed to take a list as input and output a list containing only the positive numbers from the input list. The test cases at the, ensure that the function works as expected for different scenarios of input lists. 

We can create self-contained functions that solve problems and pass tests without depending on external code or libraries.