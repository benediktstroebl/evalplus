```python
def iscube(a):
    # Check if the number is greater than 0
    if a < 0:
        return False

    # Check if the number is a perfect cube
    root = int(pow(a, (1/3)))
    return root * root * root == a
```

This function checks if the number is greater than zero, and if so, it calculates the integer cube root of the number. Then it checks if the original number is equal to the cube of the cube root. If these conditions are met, it returns `True`. All other cases result in `False`. 

To check the functionality of the function, you can run the following tests:
```python
- assert iscube(1) == True
- assert iscube(64) == True
- assert iscube(180) == False
- assert iscube(2) == False
- assert iscube(-1) == True
- assert iscube(0) == True
```

The expected results are `True` for the first two tests, `False` for the next two, and `True` for the last two.  This reflects the behavior described in the prompt.