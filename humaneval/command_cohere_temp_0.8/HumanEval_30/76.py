Here's a Python script with a self-contained function that solves the problem:
```python
def get_positive(l):
    return [x for x in l if x > 0]
```
The function `get_positive` takes a list `l` as input and returns a new list that contains only the positive elements of the original list. The list is returned as-is if all elements are positive. The function leverages list comprehension and a conditional statement to filter out elements that satisfy the condition `x > 0`. 
The `get_positive` function can be invoked with various lists to demonstrate its functionality:
```python
print(get_positive([-1, 2, -4, 5, 6]))
print(get_positive([5, 3, -5, 2, -3, 3, 9, 0, 123, 1, -10]))
```
The expected output for the given input is:
```
[2, 5, 6]
[5, 3, 2, 3, 9, 123, 1]
```
The script successfully passes the tests outlined in the original problem statement.