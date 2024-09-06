Here's a Python script with a self-contained function that solves the problem:
```python
def get_positive(l: list):
    return [x for x in l if x > 0]
```
This function uses a list comprehension, filtered for elements greater than zero, to return a new list that excludes negative numbers. 

To test this function, you can use the following:
```python
>>> get_positive([-1, 2, -4, 5, 6])
[2, 5, 6]
>>> get_positive([5, 3, -5, 2, -3, 3, 9, 0, 123, 1, -10])
[5, 3, 2, 3, 9, 123, 1]
```

The expected output corresponds to positive numbers included in the test case. 

This Python script defines a function `get_positive()` that takes a list `l` as input and returns a new list containing only the positive numbers from the input list. As confirmed by the test cases, this function successfully filters out all negative numbers from the input list.