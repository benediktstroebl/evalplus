Here's a Python script with a self-contained function that solves the problem:
```python
def incr_list(l: list):
    result = [x + 1 for x in l]
    return result
```
This function `incr_list` takes a list as an argument and returns a list where each element is incremented by 1. It uses a list comprehension to iterate over each element in the input list and adds 1 to it. The returned result is the list with elements incremented by 1. 

To test this function, you can call it with various lists and verify that the output is correct. Here is an example:
```python
# Test incr_list() with a simple list
l = [1, 2, 3, 4, 5]
result = incr_list(l)
print(result)
# This should print [2, 3, 4, 5, 6]

# Test incr_list() with a more complex list
l = [5, 3, 5, 2, 3, 3, 9, 0, 123]
result = incr_list(l)
print(result)
# This should print [6, 4, 6, 3, 4, 4, 10, 1, 124]
```
This shows that the `incr_list` function correctly increments every element in the list by 1. 
If you want to check again that the function works as expected you can copy and paste these tests into a Python environment of your choice. You can also add more tests to ensure that the function handles different scenarios correctly.