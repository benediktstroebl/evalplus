```python
def incr_list(l: list):
    """Return list with elements incremented by 1"""
    new_list = [x + 1 for x in l]
    return new_list

#Test case 1
assertEqual([1, 2, 3], [2, 3, 4])

#Test case 2
assertEqual([5, 3, 5], [6, 4, 6])

#Test case 3
assertEqual([5, 3, 3], [4, 3, 6])

#Test case 4
assertEqual([5, 3, 0], [5, 4, 10])

#Test case 5
assertEqual([0, 123], [1, 124])
```
The function `incr_list` creates a new list with elements from input list incremented by 1. 
It tests the five cases of the function's expected behavior.