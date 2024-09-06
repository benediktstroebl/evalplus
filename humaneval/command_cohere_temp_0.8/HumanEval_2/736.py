```python
def truncate_number(number):
    """
    Return the decimal part of the number given as parameter.
    """
    return number - int(number)
```

This function takes a float as an input and returns the decimal part of the number by subtracting the integer part of the number (obtained by rounding down the input value) from the input number. The function result is the remaining decimal part of the original number. 

To test this function, you can call it with a float value as follows:
```python
result = truncate_number(3.5)
print(result)  # Output: 0.5
``` 

This will output the decimal part of the number provided, which is 0.5. 

Please note that this function assumes that the input value is a positive floating point number. If you provide a negative number or a number with a value of zero, the function will not work as expected.