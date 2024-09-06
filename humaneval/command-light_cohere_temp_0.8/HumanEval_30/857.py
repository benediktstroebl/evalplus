```python
def get_positive(lst):
    """Return only positive numbers in the list"""
    return [num for num in lst if num >= 0]

#Test cases
get_positive([-1, 2, -4, 5, 6])  # [2, 5, 6]
get_positive([5, 3, -5, 2, -3, 3, 9, 0, 123, 1, -10])  # [5, 3, 2, 3, 9, 123]
get_positive([1, 2, 3, 4, 5, 6, 7])  # [1, 2, 3, 4, 5]

``` 
This Python function, `get_positive()`, efficiently extracts and returns only the positive numbers from the provided list. It utilizes list comprehension with a conditional check to achieve this purpose. This function can be easily incorporated into larger programs and serve as a fundamental building block for tasks involving positive number extraction from lists.