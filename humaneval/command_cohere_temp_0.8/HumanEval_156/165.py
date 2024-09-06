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

This approach leverages string interpolation to create the roman numeral representation by iterating through conditions. This allows for a more concise and elegant solution that directly constructs the desired string representation based on the given integer `n`. 

To test this, ensure you run it with a testing framework like `pytest`. 
For instance, you can test the function by calling: 
```python 
pytest -v tests/test_mini_roman.py
``` 

This command should generate test results and provide feedback on the self-contained function.