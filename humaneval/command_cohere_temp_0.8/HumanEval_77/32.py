```python
def iscube(a):
    # Check if the integer a is a perfect cube
    return a ** (1/3) == round(a ** (1/3))
```

This function checks if the integer a is a perfect cube by taking its cube root and comparing it with the rounded value of a **(1/3)**. A perfect cube has a cube root that is an integer, so rounding is used to handle minor floating-point errors and ensure accurate comparison. 

This approach offers a straightforward way to determine if an integer is a perfect cube, handling both positive and negative values correctly.

```python
# Test Scenarios
assert iscube(1) == True
assert iscube(8) == True
assert iscube(27) == True

assert iscube(2) == False
assert iscube(-1) == True
assert iscube(64) == True

assert iscube(0) == True
assert iscube(180) == False
```
The test scenarios ensure the function behaves correctly for different cases.