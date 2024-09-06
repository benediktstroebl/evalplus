```python
def truncate_number(n): 
    """Given a positive floating point number, it can be decomposed into 
    and integer part (largest integer smaller than given number) and decimals
    (leftover part always smaller than 1).

    Return: decimal part of the number
    """
    i,d = divmod(n,10)
    return 10**i + d
```

This Python function 'truncate_number' takes a number as input and returns the decimal part of the number. It uses the common method 'divmod' to break down the number into its integer part and decimal part. It then returns the dry to the function's specification.