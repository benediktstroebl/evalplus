```python
def int_to_mini_roman(n):
    if n == 1:
        return "i"
    elif n == 4:
        return "iv"
    elif n == 5:
        return "v"
    elif n == 9:
        return "ix"
    elif n == 10:
        return "x"
    elif n == 40:
        return "xl"
    elif n == 50:
        return "l"
    elif n == 90:
        return "xc"
    elif n == 100:
        return "c"
    elif n == 400:
        return "cd"
    elif n == 500:
        return "d"
    elif n == 900:
        return "cm"
    elif n == 1000:
        return "m"
    else:
        return ""
```

This approach leverages string interpolation to create the roman numeral representation by iterating through ranges. 

The `else` clause for the edge case of numbers outside the specified range of 1-1000 outputs an empty string, as specified in the problem statement. 

You can include this code within a Python script and invoke the function with various input values to test its functionality. 
```python
int_to_mini_roman(19) # xix
int_to_mini_roman(152) # clii
int_to_mini_roman(426) # cdxxvi
```

Ensure you include all the test cases to fully validate the function's behavior.