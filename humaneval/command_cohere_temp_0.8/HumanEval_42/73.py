Here's a Python script with a self-contained function that solves the problem:
```python
def incr_list(l: list):
    result = [x + 1 for x in l]
    return result
```
This script defines a function called `incr_list` that takes a list argument and returns a list where each element is incremented by 1. It uses a list comprehension to iterate over each element in the input list and adds 1 to it, effectively incrementing it. The function then returns the modified list. 

To verify the functionality of the script, you can use the following test-cases:
```python
# Tests
assert incr_list([1, 2, 3]) == [2, 3, 4]
assert incr_list([5, 3, 5, 2, 3, 3, 9, 0, 123]) == [6, 4, 6, 3, 4, 4, 10, 1, 124]
```

These test cases confirm that the `incr_list` function is working as expected, as it returns the anticipated modified lists for the given input lists.