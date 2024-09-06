```python
def truncate_number(number):
    """
    Return the decimal part of the number given as parameter.
    """
    return number - int(number)
```
This function simply subtracts the integer part of the number from the original number, leaving behind the decimal part, and returns it. 

To test this function, you can call it with a float input like so: 
```python
input_number = 3.5
result = truncate_number(input_number)
print(result)  # Expected output: 0.5
``` 

The output will be 0.5, which is the decimal part of the original number.