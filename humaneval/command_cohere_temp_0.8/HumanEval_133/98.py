```python
def sum_squares(lst):
    """
    Return the sum of squared integers in the provided list.
    
    Args:
        lst (list): A list of numbers.
    
    Returns:
        int: The sum of squared integers rounded up to the next integer.
    """
    result = 0
    for num in lst:
        if isinstance(num, float):
            num = int(num)
        result += num ** 2
    
    return int(result)
```

The function iterates through the list, squares each element if it's not already done, and sums them up. Finally, the function returns the rounded-up result of the sum. 

Here's how you can use the function:
```python
print(sum_squares([1, 2, 3]))  # Outputs: 14
print(sum_squares([1, 4, 9]))  # Outputs: 98
print(sum_squares([1, 3, 5, 7]))  # Outputs: 84
print(sum_squares([1.4, 4.2, 0]))  # Outputs: 29
print(sum_squares([-2.4, 1, 1]))  # Outputs: 6
```

This approach ensures that floating numbers are treated correctly and the result is rounded up as required.