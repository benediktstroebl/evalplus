Here's a Python script with a self-contained function that solves the problem:
```python
def incr_list(l: list):
    result = [x + 1 for x in l]
    return result
```
This function `incr_list` takes a list as an argument and returns a new list with elements incremented by 1. It uses a list comprehension to iterate over each element in the input list and increments it by 1. 

To validate the functionality of the script, you can write tests as follows:
```python
# Test list [1, 2, 3]
test_list = [1, 2, 3]
result = incr_list(test_list)
assert result == [2, 3, 4]

# Test list [5, 3, 5, 2, 3, 3, 9, 0, 123]
test_list = [5, 3, 5, 2, 3, 3, 9, 0, 123]
result = incr_list(test_list)
assert result == [6, 4, 6, 3, 4, 4, 10, 1, 124]
```

The tests check if the `incr_list` function correctly increments each element of the given input list and produces the expected output. 
To run the tests, you can copy and paste them into a Python interpreter or runner, and they should pass. 
This demonstrates how the function works correctly and handles different scenarios of input lists.