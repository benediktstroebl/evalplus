```python
def iscube(a):
    # Check if the number is a perfect cube
    return a ** (1/3) == round(a ** (1/3))
```

This function `iscube()` takes an integer `a` as input and returns `True` if `a` is a perfect cube of some integer; otherwise, it returns `False`. 

The markdown code block describes the problem with some test cases; the following markdown code block shows the Python code solution alongside test cases that highlight whether the function correctly determines if the given integer is a cube or not.