Here's a Python script with a self-contained function that solves the problem:
```python
def incr_list(l: list):
    result = [x + 1 for x in l]
    return result
```
This function `incr_list` takes a list as an argument and returns a new list with its elements incremented by 1. It uses a list comprehension to iterate over each element in the input list and adds 1 to it. The result is then returned as the output. The function is self-contained and can be run as stand-alone code to increment a list. 

To verify the correctness of the function, you can run the following tests:
```python
test_list = [1, 2, 3]
result = incr_list(test_list)
assert result == [2, 3, 4]

test_list = [5, 3, 5, 2, 3, 3, 9, 0, 123]
result = incr_list(test_list)
assert result == [6, 4, 6, 3, 4, 4, 10, 1, 124]
```
These tests check the function's behavior on two different lists, ensuring that each element is incremented by 1 correctly.