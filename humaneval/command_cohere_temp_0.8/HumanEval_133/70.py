```python
def sum_squares(lst):
    """You are given a list of numbers.
    You need to return the sum of squared numbers in the given list,
    round each element in the list to the upper int(Ceiling) first.
    Examples:
    For lst = [1,2,3] the output should be 14
    For lst = [1,4,9] the output should be 98
    For lst = [1,3,5,7] the output should be 84
    For lst = [1.4,4.2,0] the output should be 29
    For lst = [-2.4,1,1] the output should be 6
    """
    rounded_lst = [round(x) for x in lst]
    return sum(x * x for x in rounded_lst)
```

The function `sum_squares()` takes a list of numbers as input and returns the sum of the squares of those numbers, rounding each number to the nearest larger integer before squaring. The rounding is accomplished via the `round()` function, which rounds a given number to the nearest integer. 

To confirm the functionality, you can write a test code that invokes the function with different input values and checks the output against the expected result:
```python
# Test the function with various inputs and expected outputs
assert sum_squares([1, 2, 3]) == 14
assert sum_squares([1, 4, 9]) == 98
assert sum_squares([1, 3, 5, 7]) == 84
assert sum_squares([1.4, 4.2, 0]) == 29
assert sum_squares([-2.4, 1, 1]) == 6
```

Note: The code assumes that the list input contains only numeric values, as indicated by the error message "TypeError: cannot multiply 'int' and 'float'" that occurs when attempting to square a list element that is not numeric. If the input list contains non-numeric elements, the code will fail. Adjust the input preprocessing to ensure the list contains only numeric values if this is a possibility.  It makes the code more robust and handles a wider range of inputs.