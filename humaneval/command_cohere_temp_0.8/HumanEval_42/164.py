Here's a Python script with a self-contained function that solves the problem:
```python
def incr_list(l: list):
    result = [x + 1 for x in l]
    return result
```
This function takes a list **l** and returns a new list where each element is incremented by 1. It uses a list comprehension to iterate over each element in the input list and adds 1 to it, effectively incrementing it. 

To follow the problem statement, we should also add a few test cases to the code to verify the function's behavior. We can use Python's `assert` statement to check that the function behaves as expected. Adding the following code will perform these tests:
```python
# Test case 1
l = [1, 2, 3]
result = incr_list(l)
assert result == [2, 3, 4]

# Test case 2
l = [5, 3, 5, 2, 3, 3, 9, 0, 123]
result = incr_list(l)
assert result == [6, 4, 6, 3, 4, 4, 10, 1, 124]
```

This way, the code will ensure the function works correctly for the given input and will raise an error if the result of the function is not as expected. 
The total lines of code for this solution are 16, which includes the function, test cases, and comments. P.S. you can easily modify the test cases to new values to test other cases and ensure the function behaves as needed with other input lists.