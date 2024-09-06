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
    return ((type(x) == int) and (type(y) == int) and (type(z) == int) and 
            (a in [x, y, z]) or 
            (b in [x, y, z]) or 
            (c in [x, y, z]))
```

This function checks if any of the sums of the two given numbers equal the third number and if the types of all input numbers are integers. Initially, the function creates three variables `a`, `b`, and `c`, where each one of them is the sum of the other two numbers. The function then checks if the variables `x`, `y`, and `z` are of the integer type and if any of the a, b, or c variables are equal to one of the input numbers x, y, or z. So, it returns true if one of the numbers is equal to the sum of the other two numbers and all numbers are integers, and returns false in any other cases. 

Here is a simple test suite for the `any_int` function that can be used to verify it works as expected:
```python
test_suite = [
    (5, 2, 7,),  # 5 + 2 == 7
    (3, 2, 2),  # 3 + 2 != 2
    (3, -2, 1),  # 3 + (-2) == 1
    (3.6, -2.2, 2),  # 3.6 + (-2.2) != 2
]

for x, y, z in test_suite:
    assert any_int(x, y, z)
```