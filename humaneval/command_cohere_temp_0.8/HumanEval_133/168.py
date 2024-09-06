```python
def sum_squares(lst):
    """
    Return the sum of squared integers in the list.
    
    Args:
        lst (list): A list of numbers.
        
    Returns:
        int: The sum of squared integers rounded up to the nearest integer.
    """
    result = sum(int(round(n)**2 for n in lst if n >= 0))
    return result
```

The function `sum_squares` takes a list of numbers, iterates through them, squares them if they are greater than or equal to 0, rounds the results up to the nearest integer, and then sums them all. The resulting sum is then returned. This aligns with the problem statement's requirement of summing the squares of integers in the list, rounded up to the nearest integer.