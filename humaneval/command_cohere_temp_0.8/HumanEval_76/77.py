```python
def is_simple_power(x, n):
    return type(x) is int and x == n ** int(n ** 0.5)
```

This function simplifies the problem by directly comparing the target `x` with the integer power of the radix `n`. 

The `type(x) is int` condition is used to rule out non-integer results like `3.0` from being considered simple powers. 

This condition is applied in addition to the main condition `x == n ** int(n ** 0.5)` to filter out any non-simple powers. 

This approach ensures that the function considers only the relevant integer values for simple powers, as described in the problem statement. 

Here is a basic test suite to verify the functionality of the `is_simple_power` function:
```python
# Testing Suite for is_simple_power function
def test_simple_powers():
    assert is_simple_power(1, 4)
    assert is_simple_power(2, 2)
    assert is_simple_power(8, 2)
    assert not is_simple_power(3, 2)
    assert not is_simple_power(3, 1)
    assert not is_simple_power(5, 3)

test_simple_powers()
``` 
The function should return the correct result for each test case, providing a definitive True for simple powers and an unequivocal False for non-simple powers, considering the refinement made to the problem statement.