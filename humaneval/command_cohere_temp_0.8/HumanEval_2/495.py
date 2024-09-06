```python
def truncate_number(number):
    """
    Return the decimal part of the number given as parameter.
    """
    return number - int(number)
```
This function simply subtracts the integer part of the number from the original number, effectively leaving only the decimal part. 

To test this script, you can call the function with the example provided in the original prompt:
```python
truncate_number(3.5)
# Expected output: 0.5
``` 
This will return 0.5, which is the decimal part of the number 3.5. 

This approach is intuitive, straightforward, and easy to implement, especially for beginners, as it uses basic arithmetic operations without requiring advanced knowledge of floating-point numbers and binary representation.