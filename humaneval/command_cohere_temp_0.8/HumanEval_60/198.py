```python
def sum_to_n(n):
    """Returns the sum of the first n integers.
    
    Args:
        n (int): Summation limit. Must be a positive integer.
    
    Returns:
        int: The sum if n is a positive integer, otherwise returns None.
    """
    # Check if n is a positive integer
    if not isinstance(n, int) or n <= 0:
        return None
    
    return sum(range(1, n + 1))
```
This script includes a comment that highlights the precondition and postcondition of the sum_to_n function, which is useful for documenting your code. Also, the unit tests are omitted, but the function still fulfills the same example tests provided in the original problem. If you would like to see the complete test code, please let me know.