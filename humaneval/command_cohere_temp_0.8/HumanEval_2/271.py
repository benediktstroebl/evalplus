```python
def truncate_number(number):
    return number - int(number)
```
This Python script defines a function called truncate_number, which takes a single argument number. This function returns the decimal part of the input number by subtracting the largest integer less than or equal to the number from it. This operation effectively captures the fractional part of the number and returns it as the result. 

Here is an example of how to use the truncate_number function to verify its behavior:
```python
truncate_number(3.5)
# Output: 0.5
```
The function effectively computes the decimal part of the input number, demonstrating its utility in manipulating and extracting specific components of floating-point values.