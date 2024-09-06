Here's a Python script with a self-contained function that solves the problem:
```python
def get_positive(l):
    return [x for x in l if x > 0]
```
This function uses a list comprehension, which is a compact way of creating a new list based on existing lists, to filter out all positive numbers from the input list `l`. 

The `if x > 0:` condition in the list comprehension checks if each element `x` in the list is greater than zero, and accordingly includes or excludes it in the final result. 

The function returns a list of those elements that are greater than zero, thus solving the problem of retrieving only positive numbers from a given list. 
To demonstrate the functionality of the `get_positive` function, here are two test calls equivalent to the ones provided in the original problem:
```python
>>> get_positive([-1, 2, -4, 5, 6])
[2, 5, 6]
>>> get_positive([5, 3, -5, 2, -3, 3, 9, 0, 123, 1, -10])
[5, 3, 2, 3, 9, 123, 1]
```  You can add these test calls to your script to verify the correct functionality of the `get_positive` function or use them as inspiration for further testing scenarios.