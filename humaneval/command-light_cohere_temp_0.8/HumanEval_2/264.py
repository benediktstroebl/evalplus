```python
def truncate_number(number: float) -> float:
    """
    Returns the decimal part of the number.
    >>> return number -max(number) // int(number)
    """
    return number.max(number) // int(number)
```
This code defines a function `truncate_number` that takes a number as an argument and returns the decimal part of the number. The function uses two methods: `number.max(number)` and `int(number)` to get the largest integer less than the number and the integer part of the number, respectively. It then returns the result of the division of the number by the integer part. 

This code is a good starting point for solving the problem. You can continue and improve it based on your needs.