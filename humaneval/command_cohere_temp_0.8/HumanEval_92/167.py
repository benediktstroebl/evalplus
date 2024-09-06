```python
def any_int(x, y, z):
    '''
    Create a function that takes 3 numbers.
    Returns true if one of the numbers is equal to the sum of the other two, and all numbers are integers.
    Returns false in any other cases.
    '''
    return x in [y+z, z+y, x+y] and all(type(i) == int for i in [x, y, z])
```

The function `any_int` takes three parameters, `x`, `y`, and `z`. It uses the in operator to check if any of the three parameters are equal to the sum of the other two parameters. The `all` function checks if all three parameters are integers. The `type` function checks if each parameter is of type `int`. The function returns `True` if one of the numbers is equal to the sum of the other two and all numbers are integers, and `False` otherwise. 

Here is a simple test suite to test the function:
```python
test_suite = [
    (5, 2, 7,), 
    (3, 2, 2),
    (3, -2, 1), 
    (3.6, -2.2, 2),
    (1, 1, 1),
    (-1, -1, -1),
    (0, 0, 0),
    (10, 10, 10),
    (7, -7, 7),
    (-7, 7, -7),
    (1, -2, 3), 
    (-1, 2, -3),
    (2, -1, 1), 
    (-2, 1, -1),
    (0, 0, 0), 
    (100, 100, 100), 
    (10, 10, 10), 
    (1, 1, 1), 
    (-1, -1, -1),
    (2, 2, 2), 
    (3, 3, 3), 
    (4, 4, 4), 
    (5, 5, 5), 
    (6, 6, 6), 
    (7, 7, 7), 
    (8, 8, 8), 
    (9, 9, 9), 
    (10, 10, 10), 
    (100, 100, 100), 
    (1, 2, 3), 
    (3, 4, 5), 
    (5, 6, 7), 
    (7, 8, 9), 
    (9, 10, 11), 
    (11, 12, 13), 
    (13, 14, 15), 
    (15, 16, 17), 
    (17, 18, 19), 
    (19, 20, 21), 
    (21, 22, 23), 
    (23, 24, 25), 
    (25, 26, 27), 
    (27, 28, 29), 
    (29, 30, 31), 
    (31, 32, 33), 
    (33, 34, 33), 
    (35, 36, 37), 
    (37, 38, 39), 
    (39, 40, 41), 
    (41, 42, 43),
    (43, 44, 45), 
    (45, 46, 47), 
    (47, 48, 49), 
    (49, 50, 51), 
    (51, 52, 53), 
    (53, 54, 53), 
    (55, 56, 57), 
    (57, 58, 57), 
    (59, 60, 61), 
    (61, 62, 63), 
    (63, 64, 65), 
    (65, 66, 67), 
    (67, 68, 69), 
    (69, 70, 71), 
    (71, 72, 73), 
    (73, 74