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
```python
incr_list([5, 3, 5, 2, 3, 3, 9, 0, 123]) # output: [6, 4, 6, 3, 4, 4, 10, 1, 124]
```

With this approach, the function directly computes the result by applying the `+ 1` increment to each list element, eliminating the need for any external variables.  This solution is concise and achieves the stated goal directly, making it both efficient and easy to understand.  The function can be easily imported in other scripts without affecting other parts of the code.