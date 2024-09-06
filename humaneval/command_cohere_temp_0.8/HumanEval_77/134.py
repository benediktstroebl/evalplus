```python
def iscube(a):
    # Check if the number is greater than 0 and equal to the cube of some int
    return a > 0 and a ** (1/3) == int(a ** (1/3))
```

This function checks if the number is greater than 0, then checks if it's a cube by taking the integer cube root of the number and checking if the result is an integer.

To test this function, you can call it with different inputs and compare the output against the expected results from the given problem description. 

For example:
```python
print(iscube(1))  # Should print True
print(iscube(2))  # Should print False
print(iscube(-1))  # Should print True
print(iscube(64))  # Should print True
print(iscube(0))  # Should print True
print(iscube(180))  # Should print False
```

The expected output for each line would be:
```
True
False
True
True
False
``` 
This should help you verify that the code works as intended.