```python
def iscube(a):
    return a ** (1/3) == int(a ** (1/3))
```
This function simplifies the equation to a single comparison, which speeds up the process. 

Here is a more detailed explanation of the steps:
1. To solve the problem, we need to check if the cube root of the input number a is an integer.
2. The cube root of a is calculated by raising a to the power of 1/3.
3. The equality check in Python compares Floating-Point Numbers, which leads to a comparison of `a ** (1/3)` and `int(a ** (1/3))`.
4. The `int` function rounds the result of `a ** (1/3)` to the nearest integer, and comparing the rounded value to the actual integer cube root will result in an equality comparison, hence the assertion `a ** (1/3) == int(a ** (1/3))`

This way, the function will return `True` if the cube root of `a` is an integer, meaning that a is a cube of some integer, and `False` otherwise. 

This approach assumes that the input is a valid integer, as stated in the note in the markdown code block. 

Also, bear in mind that in edge cases like `iscube(180.)`, the function will return `False` because although mathematical cubes can be complex, the code operates on integers only.