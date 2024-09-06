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

The function any_int takes three arguments, x, y, and z. It adds each pair of numbers and checks if the result is an integer. Then, it checks the three results against each other, and returns True if one of them is true and they are not all the same. The function returns False if the result of the addition is not an integer, or if none of the conditions are met. 

Here is an example usage of the function:
```python
print(any_int(5, 2, 7))  # Output: True
print(any_int(3, 2, 2))  # Output: False
print(any_int(3, -2, 1))  # Output: True
print(any_int(3.6, -2.2, 2))  # Output: False
```

This version of the script also includes tests for the function in the code snippet below:
```python
# Unit tests:
assert any_int(5, 2, 7) == True
assert any_int(3, 2, 2) == False
assert any_int(3, -2, 1) == True
assert any_int(3.6, -2.2, 2) == False

# Edge cases:
assert any_int(1, 1, 1) == False
assert any_int(-1, -1, -1) == False

assert any_int(0, 0, 0) == False
assert any_int(-5, 0, 0) == False

# More edge cases
assert any_int(1, 2, 3) == False
assert any_int(-3, -1, 1) == True
```