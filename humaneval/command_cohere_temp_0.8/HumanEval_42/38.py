Here's a Python script with a self-contained function that solves the problem:
```python
def incr_list(l: list):
    result = [x + 1 for x in l]
    return result
```
This function adheres to the problem's specification, incrementing each element in a given list by 1 and returning the modified list. It does so through list comprehension, creating a new list results from the old list l by adding 1 to each element. As this function relies solely on the built-in `[]` notation and primitive arithmetic, it is both standalone and efficient in solving the problem. 

This solution is tested against different inputs as per the problem statement and therefore should be able to handle any input list. 
```python
# Tests
assert incr_list([1, 2, 3]) == [2, 3, 4]
assert incr_list([5, 3, 5, 2, 3, 3, 9, 0, 123]) == [6, 4, 6, 3, 4, 4, 10, 1, 124]
assert incr_list([0, 0, 0, 5, 6, 7]) == [1, 1, 1, 6, 7, 8]
```