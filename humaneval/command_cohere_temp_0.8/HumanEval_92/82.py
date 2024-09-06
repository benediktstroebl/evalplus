```python
def any_int(x, y, z):
    '''
    Create a function that takes 3 numbers.
    Returns true if one of the numbers is equal to the sum of the other two, and all numbers are integers.
    Returns false in any other cases.
    '''
    a = x + y == z
    b = y + z == x
    c = x + z == y
    return a or b or c
```

This function evaluates the three conditions `a`, `b`, and `c`, where each one checks if any two of the numbers are equal to the sum of the third number. It then returns `True` if any of these conditions is true, and `False` otherwise. 

Here is a test drive code to test the functionality of the `any_int` function:
```python
# test drive code
test_cases = [
    (5, 2, 7,),  # expected: True
    (3, 2, 2),  # expected: False
    (3, -2, 1),  # expected: True
    (3.6, -2.2, 2),  # expected: False
]

for case in test_cases:
    print(f'{case} ➞ {any_int(*case)}')
```

Based on the provided examples, the expected output should be:
```
(5, 2, 7) ➞ True
(3, 2, 2) ➞ False
(3, -2, 1) ➞ True
(3.6, -2.2, 2) ➞ False
```