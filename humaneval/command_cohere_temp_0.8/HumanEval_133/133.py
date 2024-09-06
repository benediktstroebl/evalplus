```python
def sum_squares(lst):
    """
    Return the sum of squared integers in the list, rounding each number to the next bigger integer.

    Args:
        lst (list): A list of numbers.

    Returns:
        int: The sum of squared integers in the list.
    """

    # Handle the edge case where the list is empty
    if not lst:
        return 0

    # Use a list comprehension to square each element and round up
    rounded_lst = [math.ceil(x * x) for x in lst]

    # Calculate the sum of the squared integers
    result = sum(rounded_lst)
    return result
```

The function `sum_squares` is designed to accept a list of numbers as input and calculate the sum of squared integers in that list. To accomplish this, we use a list comprehension to square each element and round each value up to the nearest integer. Finally, we sum the resulting list to obtain the desired result. The function incorporates a check to handle scenarios where the input list is empty, ensuring that it returns 0 in such cases. 

This solution adheres to the problem statement's guidelines and achieves the desired output. It is encapsulated within a function with an informative docstring, providing clarity on its purpose and usage.