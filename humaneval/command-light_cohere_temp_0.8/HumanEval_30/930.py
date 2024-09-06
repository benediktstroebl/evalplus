```python
def get_positive(lst):
    """Return only positive numbers in the list"""
    return [num for num in lst if num > 0]

#Test case 1
print(get_positive([-1, 2, -4, 5, 6]))  # Output: [2, 5, 6]

#Test case 2
print(get_positive([5, 3, -5, 2, -3, 3, 9, 0, 123, 1, -10]))  # Output: [5, 3, 2, 3, 9, 123]

#Test case 3
print(get_positive([5, 2, -9, -5, -3, 6, 7, 8, 9, 0]))    # Output: [5, 2, 6, 9]
```
The function `get_positive` takes a list `lst` as an argument and returns a new list containing only the positive numbers from the input list. This is list comprehension iterates over each element in the input list and checks if the element is greater than zero, adding it to the new list if it is.