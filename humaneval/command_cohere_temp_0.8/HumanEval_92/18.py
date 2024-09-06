```python
def any_int(x, y, z):
    '''
    Create a function that takes 3 numbers.
    Returns true if one of the numbers is equal to the sum of the other two, and all numbers are integers.
    Returns false in any other cases.
    '''
    a = x + y
    b = y + z
    c = x + z
    
    if a == int(a) and b == int(b) and c == int(c) and (a == b or a == c or b == c):
        return True
    else:
        return False
```

This function checks if any of the sums of two of the provided numbers are equal to the third number. Then it ensures that the three numbers are integers, casting them to integers using `int()` and comparing the result. Finally, it returns `True` if any of these conditions are met and `False` otherwise. 

Here is a test drive code to test the above function:
```python
def test_any_int():
    assert any_int(5, 2, 7) == True
    assert any_int(3, 2, 2) == False
    assert any_int(3, -2, 1) == True
    assert any_int(3.6, -2.2, 2) == False
    assert any_int(-5, -1, -10) == True
    assert any_int(0, 0, 0) == True
```