```python
def get_positive(lst):
    """Return only positive numbers in the list"""
    return [num for num in lst if num > 0]

#Test case 1
print(get_positive([-1, 2, -4, 5, 6]))  # Expected Output: [2, 5, 6]

#Test case 2
print(get_positive([5, 3, -5, 2, -3, 3, 9, 0, 123, 1, -10]))  # Expected Output: [5, 3, 2, 3, 9, 123]

#Test case 3
print(get_positive([-3, -2, -1, 0, 102, -5, -4]))  # Expected Output: [-3, -2, -1]

#Test case 4
print(get_positive([9, 2, 4, 2, 7, -3]))  # Expected Output: [9, 2, 2]
```
The function `get_positive()` takes a list as input and returns a new list containing only the positive numbers from the original list. 
To test the function, we can call the function with different input lists and verify that it returns the expected output. The test cases cover a expected behavior of the function for various types of lists.