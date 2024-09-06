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

This function checks if any combination of adding two of the three numbers equals the third number. It returns a boolean value (true) if any of these conditions are true, and returns false if none of these conditions are met. To achieve this, the function uses three conditional statements to check these conditions, and returns `bool(a or b or c)` which will return true if any of `a`, `b`, or `c` are true.

Here is a simple test case to ensure that the function behaves as expected:
```python
test_cases = [[5, 2, 7], [3, 2, 2], [3, -2, 1], [3.6, -2.2, 2]]

expected_answers = [True, False, True, False]

for i in range(0, len(test_cases)):
    assert any_int(*test_cases[i]) == expected_answers[i]
```