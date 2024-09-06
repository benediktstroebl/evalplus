Here's a Python function that solves the given problem and includes informative commentary to explain its workings:
```python
def double_the_difference(lst):
    """
    Sum of squares of odd numbers in a list of integers, with negative numbers ignored.
    
    Args:
        lst (list): List of numbers.
    
    Returns:
        int: Sum of squares of odd numbers, or 0 if the list is empty or contains only even or negative numbers.
    """
    # Ensure the list contains only integers and is non-empty
    valid_numbers = [x for x in lst if x >= 0 and isinstance(x, int)]
    if not valid_numbers:
        return 0
    
    odd_numbers = [x for x in valid_numbers if x % 2 == 1]
    squared_odd = [x ** 2 for x in odd_numbers]
    
    return sum(squared_odd)
```

This function leverages list comprehension and the `isinstance` function to filter out invalid entries from the input list while ensuring the resultant list contains only valid, positive integers. Subsequently, it identifies and squares odd numbers from the filtered list, summing the results. The function returns 0 if the input list is empty or contains only even or negative numbers. 

The comment section provides a clear explanation of the problem's intention and the program's implementation, effectively aiding understanding. The function also adheres to PEP 8, Python's style guide, for neat code presentation.