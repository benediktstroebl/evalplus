```python
def sum_squares(lst):
    """Returns the sum of squared numbers in the list."""
    result = 0
    for n in lst:
        result += n**2

    return result
```
The function iterates through the list and accumulates the sum of squares of each element. This solution avoids any unnecessary rounding operations as it directly computes the desired sum based on the given specification. It adheres to the problem statement's guidelines and efficiently solves the challenge.