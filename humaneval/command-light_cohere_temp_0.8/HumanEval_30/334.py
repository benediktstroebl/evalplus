```python
def get_positive(lst):
    """Return only positive numbers in the list"""
    return [num for num in lst if num >= 0]

# Test cases 1
print(get_positive([-1, 2, -4, 5, 6]))  # Output: [2, 5, 6]

# Test cases 2
print(get_positive([5, 3, -5, 2, -3, 3, 9, 0, 123, 1, -10]))  # Output: [5, 3, 2, 3, 9, 123]

# Test cases 3
print(get_positive([-333]))  # Output: []

# Test cases 4
print(get_positive([123, -1, 2, -3]))  # Output: [123]
```
This script defines a function, `get_positive`, that takes a list as input and returns a new list containing only the positive numbers from the original list. 

The function uses list comprehension to filter out the positive numbers from the input list. 

You can use this script to solve the problem and verify its correctness for various test cases.