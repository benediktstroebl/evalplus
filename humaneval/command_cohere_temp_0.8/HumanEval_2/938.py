```python
def truncate_number(number):
    return number - int(number)
```
This function simply subtracts the integer part of the number from the input `number`. The integer part of a floating-point number is the nearest integer that is less than or equal to the number. This function works for positive numbers as per the prompt. 

To handle negative numbers or the exact integer values, you can adjust the function as follows:
```python
def truncate_number(number):
    if number == int(number):
        return 0
    elif number < 0:
        return -int(number) - 1
    else:
        return number - int(number)
```
This updated version checks if the number is already an integer, in which case it returns 0. If the number is negative, it truncates the absolute value of the number and returns a negative value. For all other positive numbers, the original logic of subtracting the integer part is used. 

Both versions above assume that the input number is a valid floating-point number. You can add additional checks to handle invalid inputs if necessary.