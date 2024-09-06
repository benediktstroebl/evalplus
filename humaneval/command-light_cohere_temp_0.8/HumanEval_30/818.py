```python
def get_positive(lst):
    """Return only positive numbers in the list"""
    return [num for num in lst if num > 0]

#Test cases
assert get_positive([-1, 2, -4, 5, 6]) == [2, 5, 6]
assert get_positive([5, 3, -5, 2, -3, 3, 9, 0, 123, 1, -10]) == [5, 3, 2, 3, 9, 123, 1]

```
This script defines a function that takes a list lst and returns a new list with only the positive numbers from the original list. It uses list comprehension with the basic if condition to filter out the positive numbers.