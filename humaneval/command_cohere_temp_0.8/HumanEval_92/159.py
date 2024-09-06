```python
def any_int(x, y, z):
    '''
    Create a function that takes 3 numbers.
    Returns true if one of the numbers is equal to the sum of the other two, and all numbers are integers.
    Returns false in any other cases.
    '''
    a = x + y
    b = x + z
    c = y + z
    return ((type(x) == int) and (type(y) == int) and (type(z) == int) and 
            (x == a or y == a or z == a) and (x == b or y == b or z == b) and (x == c or y == c or z == c))
```

The function uses logical statements to check whether three conditions are met:
1. Check if `x`, `y`, and `z` are all integers (`int` type).
2. Check if `x` is equal to the sum of `y` and `z` (`a` variable).
3. Check if `x` is equal to the sum of `y` and `z` (`b` variable).
4. Check if `x` is equal to the sum of `y` and `z` (`c` variable).

The function returns 'True' if one of these conditions is met, indicating that the sum of two of the numbers is equal to the third number. Otherwise, it returns 'False'. 

The following is a test suite that can be used to validate the functionality of the `any_int` function:
```python
# Testing any_int function
def test_any_int():
    assert any_int(5, 2, 7) == True
    assert any_int(3, 2, 2) == False
    assert any_int(3, -2, 1) == True
    assert any_int(3.6, -2.2, 2) == False

test_any_int()
```

Press Enter to run the test suite. The assert statements will check if the `any_int` function returns the correct values for the given inputs. 

To guarantee that the function performs as intended, it is advised that you include additional tests with varied input situations.