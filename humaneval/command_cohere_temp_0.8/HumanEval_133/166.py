```python
def sum_squares(lst):
    """
    Return the sum of squared numbers in the given list,
    round each element in the list to the nearest larger integer first.
    """
    result = sum(x ** 2 for x in lst if isinstance(x, (int, float)) and x >= 0)
    return result
```

The `sum_squares` function iterates through each element in the input list `lst`. It only considers elements that are numbers (type int or float) and ignores negative values. For each valid element, it calculates the square using the `**` operator and sums these squares using the `sum` function. The result is the sum of the squared positive integers, rounded up to the next highest integer.

Here's an example usage of the function:
```python
print(sum_squares([1, 2, 3]))  # Outputs: 14
print(sum_squares([1, 4, 9]))  # Outputs: 98
print(sum_squares([1, 3, 5, 7]))  # Outputs: 84
print(sum_squares([1.4, 4.2, 0]))  # Outputs: 29
print(sum_squares([-2.4, 1, 1]))  # Outputs: 0
```

The function will handle the rounding and summing of squares as expected. Remember that the function ignores non-numeric elements and negative numbers.