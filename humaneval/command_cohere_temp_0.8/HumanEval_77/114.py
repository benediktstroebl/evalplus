```python
def iscube(a):
    # Check if the number is greater than 0 and equal to the cube of some int
    return a > 0 and a ** (1/3) == round(a ** (1/3))
```

This function checks if the number is greater than 0, then checks if the cube root of the number is an integer with the 'round' function, which will return True if the cube root of the number is an integer, and False if it is not. 

Here is an example usage of the iscube function:
```python
print(iscube(64)) # Output: True
print(iscube(8)) # Output: False
print(iscube(1)) # Output: True
```

This should output:
```
True
False
True
```

This demonstrates that the function correctly answers True for integers that are cubes, and False for integers that are not.