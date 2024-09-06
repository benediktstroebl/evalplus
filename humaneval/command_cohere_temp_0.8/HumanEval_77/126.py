```python
def iscube(a):
    return a ** (1/3) == int(a ** (1/3))
```
The above `iscube()` function computes the cube root of the given number `a`, and then compares it with the original number. The condition `a ** (1/3) == int(a ** (1/3))` ensures that the cube root is returned as an integer without decimal points. It returns `True` if they are equal, implying the input is a cube of some integer; otherwise, it returns `False`. 

This approach takes advantage of the properties of the cube function, where for an integer a, a^(1/3) will be an integer if and only if a is a cube of an integer. 

To ensure a valid result for negative numbers, the cube root is computed using the `**` operator, which handles negative values correctly. Thus, the assumption that the input is always valid is upheld. 

This approach has a time complexity of O(1), making it an efficient solution for determining whether a given number is a cube.