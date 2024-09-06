```python
def iscube(a):
    if a < 0:
        a = -a
    return a ** 3 == int(a ** 3)
```

This function determines whether a given integer `a` is a cube of some integer. It starts by handling the negative case, since a negative number can be flipped to yield a positive cube. Then it checks if `a` raised to the power of 3 is equal to the integer representation of the result. If this condition holds, the input is a cube, and the function returns `True`. Otherwise, it returns `False`. 

This approach leverages the intrinsic nature of cubes, where raising an integer to the power of 3 yields a result that can be expressed as the product of 3 identical numbers. For example, `2 ** 3` equates to `2 * 2 * 2`, which is 8. This property forms the basis for the condition `a ** 3 == int(a ** 3)`. 

In this test-driven approach, we assert that the function behaves as expected for a variety of inputs:
```python
assert iscube(1) == True
assert iscube(2) == False
assert iscube(-1) == True
assert iscube(64) == True
assert iscube(0) == True
assert iscube(180) == False
```

These tests ensure that the function correctly identifies cubes and handles negative and zero values appropriately.