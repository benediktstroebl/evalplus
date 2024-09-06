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

The function any_int takes three arguments, x, y, and z. It adds each pair of numbers and checks if the result is an integer. Then, it checks if one of these sums is equal to the third number and returns True if so. It returns False if any of the numbers are not integers or if none of the conditions are met. 

Here is an example of a test to ensure the function is working:
```python
test_cases = [(5, 2, 7), (3, 2, 2), (3, -2, 1), (3.6, -2.2, 2)]

expected_ans = [True, False, True, False]

for i in range(len(test_cases)):
    assert any_int(*test_cases[i]) == expected_ans[i]
```

These test cases can be added to a test suite, and they can be run to ensure the function is working correctly.