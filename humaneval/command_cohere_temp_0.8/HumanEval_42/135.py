Here is a Python script with a self-contained function that solves the problem:
```python
def incr_list(l: list):
    result = [x + 1 for x in l]
    return result
```
This function follows the problem statement and returns a list with elements incremented by 1. 

To verify the functionality, you can run the following tests:
```python
assert incr_list([1, 2, 3]) == [2, 3, 4]
assert incr_list([5, 3, 5, 2, 3, 3, 9, 0, 123]) == [6, 4, 6, 3, 4, 4, 10, 1, 124]
```
These tests check if the function works for both single-digit and multi-digit numbers, regardless of their frequency in the list.