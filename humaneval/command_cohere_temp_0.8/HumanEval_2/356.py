```python
def truncate_number(number):
    """
    Return the decimal part of the number given as parameter.
    """
    return number - int(number)
```
This function simply converts the float to an int and then returns the difference, which results in the decimal part of the original number. 

To test this script, you can call the function with a float, and the output will be the decimal part of the number. For example:
```python
truncate_number(3.5)  # Expected output: 0.5
``` 

The fundamental idea behind the function is that a float can be represented as a whole number and a decimal part, and the function returns the decimal part of the number, which is essentially the difference between the original number and the whole number part.