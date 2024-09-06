```python
def sum_squares(lst):
    """
    Return the sum of squared integers in the list, rounding each number to the next higher integer.
    """
    result = 0
    for num in lst:
        result += num ** 2
    return sum(map(round, lst))
```