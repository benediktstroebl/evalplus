Here's a Python script with a self-contained function that solves the problem:
```python
def get_positive(l: list):
    return [x for x in l if x > 0]
```
This function uses a list comprehension, filtered for elements greater than zero, to return a new list containing only positive numbers from the input list `l`. 
The function skips zero since it is neither positive nor negative. Please note list comprehension is available in Python 1.9.0 and later.

This solution will return the expected output for the given test cases, like this:
```python
>>> get_positive([-1, 2, -4, 5, 6])
[2, 5, 6]
>>> get_positive([5, 3, -5, 2, -3, 3, 9, 0, 123, 1, -10])
[5, 3, 2, 3, 9, 123, 1]
```

The function is straightforward to use and does not require any additional dependencies or external logic. It simply filters out the positive numbers from the list, making it a self-contained solution for the problem.