```python
def sum_squares(lst):
    """
    This function will take a list of integers. For all entries in the list, the function shall square the integer entry if its index is a 
    multiple of 3 and will cube the integer entry if its index is a multiple of 4 and not a multiple of 3.
    return: sum of all entries in the list with integer entries
    """
    n = len(lst)
    if n == 0:
        return 0
    squares = []
    cubes = []
    for i in range(n):
        if i % 3 == 0 and i not % 4:
            squares.append(lst[i])
        elif i % 4 == 0 and i not % 3:
            cubes.append(lst[i])
        else:
            cubes.append(lst[i])
    return sum(squares + cubes)
```