Here's a Python script with a self-contained function that solves the problem:
```python
def get_positive(l: list):
    return [x for x in l if x > 0]
```
This function uses a list comprehension, filtered for elements greater than zero, to return a new list containing only positive numbers from the input list `l`. 
The function works correctly with tests provided in the problem statement:
```python
>>> get_positive([-1, 2, -4, 5, 6])
[2, 5, 6]
>>> get_positive([5, 3, -5, 2, -3, 3, 9, 0, 123, 1, -10])
[5, 3, 2, 3, 9, 123, 1]
``` 
The function is entirely self-contained in that it does not make use of any external variables or dependencies. It simply returns the positive numbers filtered from the input list `l`.