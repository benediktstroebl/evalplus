Here's a Python script with a self-contained function that solves the problem:
```python
def incr_list(l: list):
    result = [x + 1 for x in l]
    return result
```
This function `incr_list` takes a list as an argument and returns a new list with elements incremented by 1. It uses a list comprehension to iterate over each element in the input list and increments it by 1. 

The script doesn't include tests because it's a self-contained script aimed at solving the specified problem. However, if you want to add tests to it, you can add test cases as given in the prompt like this:
```python
# Tests
assert incr_list([1, 2, 3]) == [2, 3, 4]
assert incr_list([5, 3, 5, 2, 3, 3, 9, 0, 123]) == [6, 4, 6, 3, 4, 4, 10, 1, 124]
``` 
The function is then called with different lists to test for correctness. 
The script ensures the function behaves as expected with different input lists. Futher tests can be added to validate the function's behavior on more complex scenarios if needed. 
The function's docstring can be copied as is from the original response to describe the function.