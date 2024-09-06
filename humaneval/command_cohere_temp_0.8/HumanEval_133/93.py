```python
def sum_squares(lst):
    """
    Return the sum of squared integers in the list.
    
    Round each number to the nearest larger integer first.
    """
    result = sum(int(round(n) ** 2 for n in lst))
    return result
```

This Python script defines a function called `sum_squares` which takes in a list as an input. This function returns the sum of the squares of the integers in the list. Before calculating the sum of the squares, each element in the list is rounded up to the nearest larger integer. The result is then returned as the output. 

This solution assumes that the list contains purely numerical values. If the list contains any non-numerical values, an error will occur.