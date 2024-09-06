```python
def iscube(a):
    # Check if the number is greater than 0 and equal to the cube of some integer
    return a > 0 and a ** (1/3) == round(a ** (1/3))
```

This function checks if the number is greater than 0, then checks if the `**(1/3)` power of the number is equal to the rounded version of the `**(1/3)` power of the number. If these two values are equal, then the number is the cube of some integer, otherwise it is not. 

This approach uses ``**(1/3)`` power to eliminate the need for integer divisions, making the code more efficient and simpler.