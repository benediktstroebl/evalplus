Here's a Python script with a self-contained function that solves the problem:
```python
def incr_list(l: list):
    result = [x + 1 for x in l]
    return result
```
This function `incr_list` takes a list as an argument and returns a list where each element is incremented by 1. It uses a list comprehension to iterate over each element in the input list and adds 1 to it. The return value is a new list with the incremented elements. 

To test this function, you can call it with various lists and verify that the output list contains the expected incremented values:
```python
# Test Incr_list function
assert incr_list([1, 2, 3]) == [2, 3, 4], "Incorrect incrementation"
assert incr_list([5, 3, 5, 2, 3, 3, 9, 0, 123]) == [6, 4, 6, 3, 4, 4, 10, 1, 124], "Incorrect incrementation"
```

This script provides a clear and concise way to solve the problem and pass the given tests. Let me know if it fits the requirements or if you'd like me to adjust it further. Feel free to ask if you'd like more details or further customization.