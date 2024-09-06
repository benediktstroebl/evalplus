Here's a Python script with a self-contained function that solves the problem:
```python
def incr_list(l: list):
    result = [x + 1 for x in l]
    return result
```
This script defines a function called `incr_list` that takes a list `l` as input and returns a new list where each element is incremented by 1. It uses a list comprehension to iterate over each element in the input list and adds 1 to it, effectively incrementing it. 
The function is self-contained and can be executed independently, and can be used in other scripts as a utility function for incrementing list elements. 

To test this function, you can call it with various lists and verify that the returned list contains the expected results. Here is an example: 
```python
# Test incr_list function
assert incr_list([1, 2, 3]) == [2, 3, 4]
assert incr_list([5, 3, 5, 2, 3, 3, 9, 0, 123]) == [6, 4, 6, 3, 4, 4, 10, 1, 124]
``` 
This tests the function with two different lists, verifying that the result list is correctly incremented. In the markdown code block, I will provide the code for testing the function with the `assert` statement, which is not usually included in regular documentation.