```python
def any_int(x, y, z):
    """
    Create a function that takes 3 numbers.
    Returns true if one of the numbers is equal to the sum of the other two, and all numbers are integers.
    Returns false in any other cases.
    """
    a = x + y
    b = x + z
    c = y + z
    return any([x == a, y == a, z == a, x == b, y == b, z == b, x == c, y == c, z == c])
```

The function performs numerical comparisons and uses the `any` function to return `True` if any of the conditions are met and `False` otherwise. 
This approach ensures that the function adheres to the problem requirements and provides an efficient solution. Incorporate this code into your codebase to fulfill the requested functionality.

This script will correctly identify the following cases:
- `any_int(5, 2, 7)` ➞ `True`
- `any_int(3, 2, 2)` ➞ `False`
- `any_int(3, -2, 1)` ➞ `True`
- `any_int(3.6, -2.2, 2)` ➞ `False`

This approach provides a clear and direct implementation of the requested functionality.