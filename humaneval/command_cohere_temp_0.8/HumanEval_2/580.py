```python
def truncate_number(number):
    """
    Return the decimal part of the number given as parameter.
    """
    return number - int(number)
```
This function simply subtracts the integer part of the number from the original number, effectively leaving only the decimal part. 

To test this script, you can call the function with a float input argument, and the output will be the decimal part of the input number. 

For example:
```python
truncate_number(3.5)  # Expected output: 0.5
``` 
or 
```python
truncate_number(12.34567)  # Expected output: 0.34567
```  You can add this code to a Python file and run it to see the output.