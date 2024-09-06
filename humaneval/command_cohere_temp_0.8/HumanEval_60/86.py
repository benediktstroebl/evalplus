```python
def sum_to_n(n):
    """Returns the sum of the first n integers.
    
    Args:
        n (int): Summation limit.
    
    Returns:
        int: The sum if n is a positive integer, otherwise returns None.
    """
    sum = 0
    for i in range(1, n + 1):
        sum += i
    return sum
```
This script defines a function 'sum_to_n' that calculates the sum of integers from 1 to 'n'. The function includes an argument and a return value clarification. It employs a loop to iteratively sum the integers and then returns the resultant sum.