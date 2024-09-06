Here's a Python script with a self-contained function that solves the problem:
```python
def incr_list(l: list):
    result = [x + 1 for x in l]
    return result
```
This function uses a list comprehension to iterate over each element in the input list and increment it by 1. The new incremented element is then returned in a new list. 

To verify the correctness of the function, two test cases are provided:
```python
# Test case 1
l = [1, 2, 3]
expected = [2, 3, 4]
result = incr_list(l)
assert result == expected

# Test case 2
l = [5, 3, 5, 2, 3, 3, 9, 0, 123]
expected = [6, 4, 6, 3, 4, 4, 10, 1, 124]
result = incr_list(l)
assert result == expected
```
These tests ensure that the `incr_list` function works correctly for different scenarios.