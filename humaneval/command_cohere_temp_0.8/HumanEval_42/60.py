Here's a Python script with a self-contained function that solves the problem:
```python
def incr_list(l: list):
    result = [x + 1 for x in l]
    return result
```
This script defines a function called `incr_list` that takes a list `l` as input and returns a new list where each element is incremented by 1. It uses a list comprehension to iterate over each element in the input list and adds 1 to it, effectively incrementing it. The function outputs are:
```python
[2, 3, 4]
[6, 4, 6, 3, 4, 4, 10, 1, 124]
```
The function is self-contained and can be used directly to increment elements in a list.  It is scoped to the function, meaning the variable `result` is only accessible within the `incr_list` function.  It eliminates the need for an external variable to store the result, making it more efficient and safer, avoiding potential naming conflicts or unintended accessibility issues.