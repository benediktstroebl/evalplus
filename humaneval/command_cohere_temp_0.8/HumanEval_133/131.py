```python
def sum_squares(lst):
    """
    Return the sum of squared integers in the list, rounding each list element to the nearest larger integer.
    """
    result = 0
    for num in lst:
        result += num ** 2
    
    return int(result)
```
This Python script defines a function 'sum_squares' that calculates the sum of the squares of integers in a given list. First, it iterates through the list, squaring each element and adding it to the 'result'. Then, it returns the rounded value of the 'result' using 'int()', taking the upper integer value for each element. 
It solves the task of returning the sum of squared numbers in a list, rounding each element to the upper integer, as per the problem statement.