```python
def sum_to_n(n):
    """Returns the sum of the first n integers.
    
    Args:
        n (int): Summates integers up to this value.
        
    Returns:
        int: Sum of integers from 1 to n.
    """
    return sum(range(1, n + 1))
```

The function uses the `range()` function to generate a series of numbers from 1 to `n` (inclusive). Then, the `sum()` function adds all the numbers in the generated series, giving the desired result. 

This approach gives a clear and concise solution to the problem, avoiding any unnecessary complexity. 

You can add your own test cases to further verify the function's behavior and ensure it meets your needs in various scenarios. 
If needed, the script can be adapted to include the additional tests as well.