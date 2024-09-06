```python
def any_int(x, y, z):
    '''
    Create a function that takes 3 numbers.
    Returns true if one of the numbers is equal to the sum of the other two, and all numbers are integers.
    Returns false in any other cases.
    '''
    a = x + y == z
    b = y + z == x
    c = x + z == y
    return bool(a or b or c)
```

This function checks if any combination of adding two of the three numbers equals the third number. The result is true if any of these conditions are true, and false otherwise. The 'or' logic returns true if any of the three conditions are true.

This problem can also be solved using python's `set` theory and `powerset` function, but it is not as efficient with space as the previous `ternary` condition solution. Here is an example:
```python
def any_int(x, y, z):
    integers = set([x, y, z])
    return any(a + b == c for a, b, c in itertools.permutations(integers, 3))
```
This solution uses `itertools.permutations` to generate all possible combinations of the three numbers, and the `set` theory checks if one of the sums equals the third number.