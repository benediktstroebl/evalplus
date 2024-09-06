Here's a Python script with a self-contained function that solves the problem:
```python
def incr_list(l: list):
    result = [x + 1 for x in l]
    return result
```
This script defines a function called `incr_list` that takes a list parameter `l`. It then returns a new list where each element from the input list `l` is incremented by 1. It uses a list comprehension to iterate over each element in the input list and adds 1 to it, then includes it in the output list. 

You can call this function with an input list to see its behavior:
```python
incr_list([1, 2, 3]) # Output: [2, 3, 4]
```
Or any other list:
```python
incr_list([5, 3, 5, 2, 3, 3, 9, 0, 123]) # Output: [6, 4, 6, 3, 4, 4, 10, 1, 124]
```

This solution is efficient and has a time complexity of `O(n)` since it processes each element of the list once, resulting in a new list with the elements incremented by 1.