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

This function evaluates the 3 conditions mentioned in the problem statement and returns 'True' if any of them are 'True'. Otherwise, it returns 'False'.

Here is a test drive code to test the functionality of the function:
```python
test_drive = '''
test_cases = [
    (5, 2, 7,),  # true
    (3, 2, 2),  # false
    (3, -2, 1),  # true
    (3.6, -2.2, 2),  # false
]

for case in test_cases:
    print(f'{case} => {any_int(*case)}')
'''

exec(test_drive)
```

Expected output:
```bash
(5, 2, 7) => True
(3, 2, 2) => False
(3, -2, 1) => True
(3.6, -2.2, 2) => False
```