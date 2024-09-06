```python
def get_positive(l: list):
    return [num for num in l if num >= 0]

#Test case 1
assert get_positive([-1, 2, -4, 5, 6]) == [2, 5, 6]

#Test case 2
assert get_positive([5, 3, -5, 2, -3, 3, 9, 0, 123, 1, -10]) == [5, 3, 2, 3, 9, 123, 1]
```

This Python script defines a function `get_positive` that filters out negative numbers from an input list. It uses list comprehension and iterating through a list and returns a new list with only positive numbers. The test cases demonstrate the the result of the function for different input lists.