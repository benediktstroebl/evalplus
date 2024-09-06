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

    if not isinstance(x) or not isinstance(y) or not isinstance(z):
        return False
    
    if a in (b, c) and a == int(a):
        return True
    
    return False
```

The function employs three conditional statements to check if `a` equals either `b` or `c`, and that all variables are integers. The function returns true if one of these conditions is met, and false otherwise. 

To test this function, consider using the following Python code:
```python
# Test 1
print(any_int(5, 2, 7))  # Expected output: True

# Test 2
print(any_int(3, 2, 2))  # Expected output: False

# Test 3
print(any_int(3, -2, 1))  # Expected output: True

# Test 4
print(any_int(3.6, -2.2, 2))  # Expected output: False
```

This should help you verify the correctness of the function. Let me know if you need anything else!