Here's a Python script with a self-contained function that solves the problem:
```python
def get_positive(l):
    return [x for x in l if x > 0]
```
This function uses a list comprehension, which is a short way of writing a for loop, to create a new list with only the positive numbers from the input list `l`. 

The markdown code block would look like this:
```python
def get_positive(l):
    return [x for x in l if x > 0]
```
This script will return a list containing only the positive numbers from the input list, which could be `[5, 3, -5, 2, -3, 3, 9, 0, 123, 1, -10]` for the provided examples. The function will return the list `[5, 3, 2, 3, 9, 123, 1]`.