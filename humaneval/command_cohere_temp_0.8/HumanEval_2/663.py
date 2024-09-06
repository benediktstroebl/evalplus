```python
def truncate_number(number):
    """
    Return the decimal part of the number given as parameter.
    """
    return number - int(number)
```
This function simply converts the float number to an integer (using int function), and subtract the result from the original number, thus returning the fractional part (the decimals). 

To test this script you can call the function with a floating point number as follows: 
```python
truncate_number(3.5)  # Expected output: 0.5
``` 
or with any other floating point number. 

The script fully adheres to the problem statement, fulfilling the requirements of returning the decimal part of the number given as input. 
Let me know if it suits your needs!