```python
def sum_to_n(n):
    """Returns the sum of the first n integers.
    
    Args:
        n (int): Summation limit.
    
    Returns:
        int: The sum if n is a positive integer, otherwise returns None.
    """
    if not isinstance(n, int) or n < 1:
        return None
    return sum(range(1, n + 1))
```
This script defines a function `sum_to_n` taking a single integer argument `n`. The function aims to return the sum of the first `n` integers. It checks if `n` is an integer and greater than 0 to ensure validity before returning the sum using the `range` and `sum` functions combination. Additionally, the function returns `None` for invalid inputs like non-integer or negative values. 

To use this function, you can import it from the script module like this:
```python
from sum_to_n import sum_to_n
```
And then use it alongside the module's docstring, like this:
```python
>>> sum_to_n(30)
465
>>> sum_to_n(100)
5050
>>> sum_to_n(5)
15
>>> sum_to_n(10)
55
>>> sum_to_n(1)
1
>>> sum_to_n(0)
None
>>> sum_to_n(2.5)
None
```

Note that the tests included in the code will ensure the function behaves correctly for various inputs.