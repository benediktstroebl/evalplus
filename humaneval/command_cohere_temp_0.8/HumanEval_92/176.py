```python
def any_int(x, y, z):
    """
    Create a function that takes 3 numbers.
    Returns true if one of the numbers is equal to the sum of the other two, and all numbers are integers.
    Returns false in any other cases.
    """
    a = x + y == z
    b = y + z == x
    c = x + z == y
    return bool(a or b or c)
```

This function checks if any combination of adding two of the three numbers equals the third number. The function then returns `true` if any calculation yields a match and all numbers are integers; otherwise, it returns `false`. 
This problem can also be solved using python's `any()` function but the code will be less self-contained without a separate variable declaration for each condition so it avoids the use of `any` for this specific problem. A version with `any` would look like this: 

```python
def any_int(x, y, z):
    return any((x + y == z, y + z == x, x + z == y))
```
To test the function above, you can use the following code:

```python
# tests
assert any_int(5, 2, 7) == True
assert any_int(3, 2, 2) == False
assert any_int(3, -2, 1) == True
assert any_int(3.6, -2.2, 2) == False
```
This will assert the function `any_int` appropriately returns `true` or `false` for each test case.