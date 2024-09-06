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
    else:
        return False
```

The function uses conditional statements to check whether the sum of any two of the integers is equal to the third integer. To ensure that the function works perfectly, the condition that checks whether the numbers are integers is checked using the `isinstance()` function. The function returns true if one of the sums matches the third number and all numbers are integers, and false in any other case. 

Here is a simple test suite that can be used to test the function:
```python
# Testing any_int function
def test_any_int():
    assert any_int(5, 2, 7) == True
assert any_int(3, 2, 2) == False
assert any_int(3, -2, 1) == True
assert any_int(3.6, -2.2, 2) == False
```

The test suite contains 4 tests, each testing a different scenario. The `assert` statement ensures that the tested scenario is correctly solved by the `any_int` function.  In other words, the `assert` statement will throw an error if the opposite of the expression following the statement is true.