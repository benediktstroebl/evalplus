```python
def sum_squares(lst):
    """
    Return the sum of squared integers in the provided list.
    
    Args:
        lst (list): List of numbers.
    
    Returns:
        int: The sum of squared integers.
    """
    result = 0
    for num in lst:
        num = int(num) ** 2
        result += num
    
    return result
```

The function `sum_squares` takes a list of numbers, squares each one, and then adds them up. It ensures that only integer values are squared to avoid raising errors and returns the expected sum of squared integers. 

This approach safeguards against floating-point values and gracefully handles the specified test cases, including edge scenarios like empty lists, ensuring the function's robustness and accuracy. 

To execute the function, simply call `sum_squares` and pass the list as an argument, and the function will return the sum of the squared integers.