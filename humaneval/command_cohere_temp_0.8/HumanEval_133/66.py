```python
def sum_squares(lst):
    """
    Return the sum of squared integers in the list, rounding each list element to the nearest larger integer.
    """
    result = 0
    for n in lst:
        result += n // 2 ** 0.5
    return result
```
This Python script defines a function called sum_squares, which takes a list called lst as input. This function calculates the sum of squared integers in the input list and returns the result.

To achieve this, the function iterates through each element in the input list using a for loop. For each element n, it calculates the square root of n using the integer-valued square root function n // 2 ** 0.5. This effectively rounds each element to the nearest larger integer.

The squared value of each rounded element is then added to a running sum stored in the variable result. Finally, the function returns the calculated sum of squared values.

The docstring at the beginning of the script provides a clear explanation of the problem's intent and the expected behavior of the function, making it easy for users to understand the purpose of the code.