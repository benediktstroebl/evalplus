Here's a Python script with a self-contained function that solves the problem:
```python
def incr_list(l: list):
    result = [x + 1 for x in l]
    return result
```
This script defines a function called `incr_list` that takes a list `l` as input and returns a new list where each element is incremented by 1. It uses a list comprehension to iterate over each element in the input list and adds 1 to it, effectively incrementing it. The function outputs are:
```python
>>> incr_list([1, 2, 3])
[2, 3, 4]
>>> incr_list([5, 3, 5, 2, 3, 3, 9, 0, 123])
[6, 4, 6, 3, 4, 4, 10, 1, 124]
```
These outputs match the specified examples in the problem statement. The function is self-contained and does not rely on any external variables or assumptions. It simply takes the input list and returns the expected result. 
If you have additional tests you want to run to confirm the function's behavior, you can do so by adding them within the test parentheses. GIVEN_LIST]) ]}}