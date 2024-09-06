Here's a Python script with a self-contained function that solves the problem:
```python
def incr_list(l: list):
    result = [x + 1 for x in l]
    return result
```
This function takes a list **l** and returns a new list where each element is incremented by 1. 

Here is an example of how to use this function:
```python
incr_list([1, 2, 3]) # output: [2, 3, 4]
```
The function can also take a list like `[5, 3, 5, 2, 3, 3, 9, 0, 123]` and return a new list like `[6, 4, 6, 3, 4, 4, 10, 1, 124]`. 

This approach uses list comprehension, which makes the code more concise and easier to understand.