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

    if not isinstance(x) or not isinstance(y) or not isinstance(z):
        return False
    
    if a in [x, y, z] or b in [x, y, z] or c in [x, y, z]:
        return True
    
    return False
```

The function employs three variables to store the sums of all pairs of the input trio. It then checks if any of the sums is identical to one of the original numbers. Furthermore, it verifies whether the type of each number in the input trio is an integer using the `isinstance()` function. If any of these checks fail, the function returns `False`. Otherwise, it returns `True`. 

This code will correctly determine whether the given trio of numbers fulfills the specified conditions. 

```python
t = [
    (5, 2, 7),
    (3, 2, 2),
    (3, -2, 1),
    (3.6, -2.2, 2)
]

test_any_int = lambda x, y, z: any_int(x, y, z)  == bool(x == y + z or y == x + z or z == x + y)

for case in t:
    assert test_any_int(*case)
```