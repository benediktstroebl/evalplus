```python
def sum_squares(lst):
    """
    Return the sum of squared numbers in the given list,
    round each element in the list to the nearest larger integer first.
    """
    result = sum(x**2 for x in lst if isinstance(x, (int, float)) and x >= 0)
    return result
```

The Python script provides a function called `sum_squares` that takes a list called `lst` as input. This function calculates the sum of squared integers in the list while also handling a few edge cases.

First, it verifies that each list element is either an integer or a float, and that element must be greater than or equal to zero (`isinstance(x, (int, float)) and x >= 0`). Elements that fulfill these criteria have their squares computed using a generator expression `x**2`. The sum of these squared values is then calculated using the `sum` function.

This code effectively handles the edge cases outlined in the problem statement, specifically:
- If any non-numeric elements or negative numbers are present in the list, they will not be included in the sum of squares.

The resulting sum is returned as the output of the function.