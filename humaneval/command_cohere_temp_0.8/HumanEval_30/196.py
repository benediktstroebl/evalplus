```python
def get_positive(l: list):
    return [x for x in l if x > 0]
```

The function `get_positive` takes a list `l` as an argument and returns a list of all positive numbers in that list. The python for loop syntax and logic is used to create a new list that contains only the elements that satisfy the condition `x > 0`. The new list is then returned. 

This solution corresponds to the problem description and solves the given task. It should work correctly for any list that contains either positive or negative numbers. 

```python
# TEST CASES
assert get_positive([-1, 2, -4, 5, 6]) == [2, 5, 6]

assert get_positive([5, 3, -5, 2, -3, 3, 9, 0, 123, 1, -10]) == [5, 3, 2, 3, 9, 123, 1]
``` 

These tests ensure that the function `get_positive` correctly extracts all positive numbers from a list, regardless of the list's content and size.