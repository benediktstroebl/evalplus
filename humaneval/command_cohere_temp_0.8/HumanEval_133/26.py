```python
def sum_squares(lst):
    """
    Return the sum of squared numbers in the given list,
    round each element in the list to the nearest upper int first.
    """
    result = sum(int(rounding(n)) ** 2 for n in lst for rounding in (lambda x: x, lambda x: x + 0.5, lambda x: x - 0.5) if int(rounding(n)) ** 2)
    return result
```

The function `sum_squares` iterates through the list, attempting to round each number to the nearest upper integer using three different rounding strategies. For instance, the value 4.2 is rounded to 4, 5, and 6 using the rounding functions `lambda x: x, lambda x: x + 0.5, lambda x: x - 0.5`. The sum of the squared values is then calculated using a generator expression, filtering out non-integer values and invalid rounding strategies. 

Here's a shorter version of the code using the `map` function to iterate over the list:
```python
def sum_squares(lst):
    return sum(int(n) ** 2 for n in map(round, lst))
```

This version uses the `map` function to apply the `round` function to each element in the list `lst`. The rounded values are then converted to integers and squared to calculate their sum.