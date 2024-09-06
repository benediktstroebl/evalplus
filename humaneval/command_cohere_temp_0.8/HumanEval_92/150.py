```python
def any_int(x, y, z):
    """
    Create a function that takes 3 numbers.
    Returns true if one of the numbers is equal to the sum of the other two, and all numbers are integers.
    Returns false in any other cases.
    """
    a = x + y
    b = y + z
    c = x + z
    
    if a == int(a) and b == int(b) and c == int(c) and (a == b or a == c or b == c):
        return True
    else:
        return False
```

The function any_int takes three arguments, x, y, and z. It adds each pair of numbers and checks if the result is an integer. Then, it checks the three results against each other, and returns True if one of them is true and they are not all the same. The function returns False if none of these conditions are met, which happens when either not all numbers are integers or when the three sums are not equal to each other. 

To test this function, run the following code: 

```python
# Tests
assert any_int(5, 2, 7) == True
assert any_int(3, 2, 2) == False
assert any_int(3, -2, 1) == True
assert any_int(3.6, -2.2, 2) == False
```

Each test correctly validates the behavior of the function according to the problem description.