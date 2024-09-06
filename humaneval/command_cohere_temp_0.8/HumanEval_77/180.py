```python
def iscube(a):
    # Check if the number is greater than 0 and equal to the cube of some int
    return a > 0 and a ** (1/3) == int(a ** (1/3))
```

This function checks if the number is greater than 0, then checks if the `float(a)**(1/3)` is equal to an integer through the use of the `int()` function. 

This will correctly return True if a is the cube of some integer, and false otherwise. We use the comparison `float(a)**(1/3) ` because a**(1/3) would result in a non-integer value. 

We then use the `int()` function to round it to the nearest integer.