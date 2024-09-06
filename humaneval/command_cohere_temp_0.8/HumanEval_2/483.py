```python
def truncate_number(number):
    """
    Return the decimal part of the number given as parameter.
    """
    return number - int(number)
```
This function simply subtracts the integer part of the number from the original number, leaving behind the decimal part, and returns it. The integer part of the number is obtained using the built-in Python function int. 

To test this function, you can call it with a floating point input value like so:
```python
input_number = 3.5
result = truncate_number(input_number)
print(result)  # Expected output: 0.5
``` 

The provided example test case would yield the desired output of 0.5. 

This approach utilizes basic arithmetic operations to simply peel away the integer part of the number, effectively leaving behind the desired decimal component. 
The docstring, or function description, explains the purpose and behavior of the function, and provides examples to illustrate its usage. 
This approach ensures the function is self-contained, easily understood, and ready to utilize in broader code bases.