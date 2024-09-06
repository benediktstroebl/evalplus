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
    if a in [x, y, z] or b in [x, y, z] or c in [x, y, z]:
        return True
    elif type(x) is not int or type(y) is not int or type(z) is not int:
        return False
    else:
        return False
```
The function any_int takes three arguments, x, y, and z. It first checks if any of the sums a, b, or c are equal to x, y, or z, and if so, it returns True. It then checks if any of the elements are not integers, and if so, it returns False. If none of the above conditions are met, it returns False.

Here is an example of function usage:
```python
test_list = [
    (5, 2, 7,),  # Expected output: True
    (3, 2, 2,),  # Expected output: False
    (3, -2, 1),  # Expected output: True
    (3.6, -2.2, 2),  # Expected output: False
]

for x, y, z in test_list:
    assert any_int(x, y, z) == True
```
The any_int function should return True in the first two examples and False in the last example owing to the float number 3.6.