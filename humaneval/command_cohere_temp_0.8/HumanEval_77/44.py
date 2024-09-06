```python
def iscube(a):
    # Check if the number is greater than 0 and equal to the cube of some int
    return a > 0 and a ** (1/3) == round(a ** (1/3))
```

This function checks if the number is greater than 0, then checks if the cube root of the number is an integer with the 'round' function, which will return true if the cube root is an integer and the number is a cube. Note that this function assumes that the input is always valid, as stated in the prompt.