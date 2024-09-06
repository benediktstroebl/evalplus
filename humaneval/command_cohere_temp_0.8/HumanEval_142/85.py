```python
def sum_squares(lst):
    result = 0
    for i, num in enumerate(lst):
        if i % 3 == 0:
            result += num ** 2
        elif i % 4 == 0 and i % 3 != 0:
            result += num ** 3
    return result
```

The function sums over the list `lst` and for each entry, squares it if the index is a multiple of 3 and cubes it if the index is a multiple of 4 and not a multiple of 3. The resulting sum is then returned. 

Note that the `enumerate` function is used to simplify the process of getting the index of a list entry during the loop.

This solution passes the provided tests of the problem statement.