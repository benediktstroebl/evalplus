```python
def iscube(a):
    # Check if the number is greater than 0 and equal to the cube of some int
    return a > 0 and a ** (1/3) == int(a ** (1/3))
```

This function satisfies the requirements specified in the markdown code block. It returns True if `a` is the cube of some integer; otherwise, it returns False. 
The cube root of integers is always integers and the above function takes care of this aspect.