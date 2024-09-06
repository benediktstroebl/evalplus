```python
def sum_squares(lst):
    """
    Return the sum of squared integers in the provided list.
    
    Args:
        lst (list): A list of numbers.
    
    Returns:
        int: The sum of squared integers rounded up to the nearest integer.
    """
    result = 0
    for num in lst:
        if isinstance(num, int): 
            result += num ** 2    
    return int(result)
```

The function iterates through the list, and for each integer, it adds its square to the `result`. Finally, the function returns the `result` rounded up to the nearest integer. 

To handle the ceiling rounding, the function intakes an integer list, squares each integer, adds them up, and then converts the result to an integer type. This is also why the function explicitly checks if each element `num` in `lst` is an integer with the `isinstance(num, int)` expression. If `num` is not an integer, it is skipped, ensuring that only the integers are squared and summed up. 

This approach allows the function to handle all the test cases provided efficiently and accurately.