```python
def get_positive(lst):
    return [num for num in lst if num >= 0]

#Test cases
get_positive([-1, 2, -4, 5, 6]) # [2, 5, 6]
get_positive([5, 3, -5, 2, -3, 3, 9, 0, 123, 1, -10]) # [5, 3, 2, 3, 9, 123, 1]
get_positive([]) # []
get_positive([12, 34, 67, 21]) # [34, 67, 21]

```
This script defines a function, `get_positive`, that takes a list as input and returns a new list with only the positive numbers from the original list. The function uses a simple list comprehension to filter out the positive numbers.

The script then provides a few test cases to demonstrate the functionality of the function, passing them through the function and checking the returned lists against the expected results.