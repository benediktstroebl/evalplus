```python
def sum_squares(lst):
    """
    Return the sum of squared integers in the list.
    
    Args:
        lst (list): A list of numbers.
        
    Returns:
        int: The sum of squared integers rounded up to the nearest integer.
    """
    result = 0
    for n in lst:
        rounded_n = int(n**2)**0.5
        result += rounded_n
    return result
```

The function `sum_squares` takes a list of numbers, squares each number, takes the square root to round it up to the nearest integer, and adds it to the result. It implies that the sum of the list of integers would be returned if it had been squared. The function complies with the problem statement by rounding each number in the list to the nearest integer before adding their squares. 

To ensure the function performs as expected, it is recommended to handle corner cases such as an empty list or a list containing floating point numbers to verify the behavior. You can also test with a list containing values that are already perfect squares to ensure they are not rounded incorrectly.