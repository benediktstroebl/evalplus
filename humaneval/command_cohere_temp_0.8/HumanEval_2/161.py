```python
def truncate_number(number):
    return number - int(number)
```
This Python script defines a function called truncate_number, which takes a single argument number. This function returns the decimal part of the input number by subtracting the nearest integer (rounded down) from the input number. This effectively removes the integer part of the number, leaving only the decimal portion. 

For example, if the function is called with the input 3.5, the result will be 0.5, as 3.5 - 3 = 0.5.

This approach utilizes basic arithmetic operations to extract the decimal part of a floating-point number.

This function is straightforward and effective, providing a simple way to retrieve the decimal portion of a number in Python.