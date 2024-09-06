Here's a Python script with a self-contained function that solves the problem:
```python
def incr_list(l: list):
    result = [x + 1 for x in l]
    return result
```
This function takes a list **l** and returns a new list where each element is incremented by 1. It uses a list comprehension to iterate over each element in the input list and increment it by 1, and the result is a new list with the incremented elements. The function is self-contained and can be executed independently, and it also provides a simple and efficient solution to the problem.  It can be executed independently to test and verify the function behavior. 
```python
incr_list([1, 2, 3])
# [2, 3, 4]
incr_list([5, 3, 5, 2, 3, 3, 9, 0, 123])
# [6, 4, 6, 3, 4, 4, 10, 1, 124]
``` 
This shows how the function behaves for different input lists.