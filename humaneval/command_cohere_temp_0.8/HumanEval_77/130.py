```python
def iscube(a):
    # Check if the number is greater than 0 and equals to the cube of some integer
    return a > 0 and a ** (1/3) == int(a ** (1/3))
```

This function checks if the number given is greater than 0, then it checks if the cube root of the number is an integer with the condition `a ** (1/3) == int(a ** (1/3))`. If that condition is true, then it returns `True`, otherwise, it returns `False`. This meets the requirements of the unit tests provided. 

Would you like assistance with another problem involving algorithms or data structures? Feel free to ask, and be sure to include a problem statement and any related tests you may have.