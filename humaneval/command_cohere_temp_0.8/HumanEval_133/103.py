```python
def sum_squares(lst):
    """
    Return the sum of squared integers in the provided list.
    
    Args:
        lst (list): List of numbers.
    
    Returns:
        int: Sum of squared integers rounded up to the nearest integer.
    """
    result = sum(int(round(n ** 2)) for n in lst)
    return result
```

The function `sum_squares` takes a list of numbers as an argument and returns the sum of the squares of these numbers, rounded up to the nearest integer. It does this by using a generator expression in conjunction with the `sum` function to calculate the sum of squared integers while rounding each number up to the nearest integer. 

To achieve this, it iterates over each number in the input list and squares each number. Then, it rounds the resulting value using the `round` function and converts it to an integer using `int`. Finally, it sums up these squared integers to obtain the desired result.