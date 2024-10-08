Here's a Python script with a self-contained function that solves the problem:
```python
def get_positive(l):
    return [x for x in l if x > 0]
```
This function uses a list comprehension, which is a compact way of creating a new list based on existing lists. In this case, it creates a new list that includes only the elements of l that are greater than zero. The expression x for x in l if x > 0 generates a list of all elements x in the list l if x is greater than zero.

You can test this function with the following calls, which are verified to match the problem's expected outputs:
```python
>>> get_positive([-1, 2, -4, 5, 6])
[2, 5, 6]
>>> get_positive([5, 3, -5, 2, -3, 3, 9, 0, 123, 1, -10])
[5, 3, 2, 3, 9, 123, 1]
```

This function is straightforward and efficient, providing a quick way to filter only positive numbers from a list.