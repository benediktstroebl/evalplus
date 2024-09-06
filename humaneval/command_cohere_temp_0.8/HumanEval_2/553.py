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
print(result)  # Output: 0.5
``` 

The expected output of 0.5 demonstrates that the function extracts the decimal part of the input number.