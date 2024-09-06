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
    return bool(a or b or c)
```

This function checks if any combination of adding two of the three numbers equals the third number. The function returns `true` if one of these conditions is met, otherwise `false`. 

Here is a test to ensure that the function behaves as intended:
```python
test = '''
any_int(5, 2, 7) ➞ True
any_int(3, 2, 2) ➞ False
any_int(3, -2, 1) ➞ True
any_int(3.6, -2.2, 2) ➞ False
'''
print(test)

for t in test.split('\n'):
    assert eval(t) == any_int(*eval(t))
```

The test code takes each line of the test string, evaluates it into a tuple of values, and compares it with the output of the `any_int` function. 

This should print:
```bash
True
False
True
False
```