```python
def iscube(a):
    # Check if the number is greater than 0 and equal to the cube of some int
    return a > 0 and a ** (1/3) == round(a ** (1/3))
```

This function checks if the number is greater than 0, then checks if the root of the number (a ** (1/3)) is an integer with the 'round' function and returns the result of this expression. As this expression returns True if the number is a cube, the function returns True in this case. Note that to use this function you need to have the 'round' function imported.

It is important to note that the 'round' function is used to evaluate the cube root value and check if it is an integer, as floating point values in Python are represented with a precision of approximately 15 decimal points, and thus, for purposes of this check, the value would be considered as not an integer. Using 'round' ensures that we evaluate the value as an integer and make the correct determination. 

However, if you are looking to optimize the function to deliver more efficient code, you may want to consider handling the case where the number is 0 separately, as the current implementation will return False for 0, despite 0 being a valid cube number. 

Here is a modified version of the function that accounts for this: 
```python
def iscube(a):
    # Check if the number is equal to 0 or a cube of some integer
    return a == 0 or a > 0 and a ** (1/3) == round(a ** (1/3))
```

This version of the function directly returns True if a is 0, which ensures that 0 is correctly identified as a valid cube number.