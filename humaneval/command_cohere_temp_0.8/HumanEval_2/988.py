```python
def truncate_number(number):
    """ Returns the decimal part of a positive floating point number. """
    return number - int(number)
```

This function takes a positive floating point number as an input, and returns the decimal part of the number. The function simply subtracts the integer part of the number from the input number and returns the result. 

To demonstrate the functionality of the function, here is an example of use:
```python
# Example of use
number = 3.5
result = truncate_number(number)

print(result)  # Output: 0.5
```

The code then checks if the result is correct using the assertion:
```python
assert result == 0.5
```

The testing framework then generates this result when the above code is executed.