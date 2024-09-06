```python
def truncate_number(number):
    return number - int(number)
```
This Python script defines a function called `truncate_number` that takes in a single argument, `number`, which is expected to be a positive floating point number. Inside the function, the `int` function is used to convert the input number to an integer, which effectively discards the decimal part of the number. The resulting integer value is then subtracted from the original input number. This subtraction operation effectively keeps only the decimal part of the original number, as the integer part of the number is canceled out due to the subtraction operation. The function then returns the decimal part of the number, which is the leftover fractionary part setup to be smaller than 1. 

Here is an example of how you can use the `truncate_number` function to truncate a positive floating point number:
```python
result = truncate_number(3.5)
print(result)  # Output: 0.5
```
In this example, the number 3.5 is passed to the `truncate_number` function. The function calculates 3.5 - int(3.5), which equals 0.5, and returns the result, yielding a output of 0.5. 

This function is useful for grabbing the decimal part of a positive floating point number, enabling manipulation and analysis of the fractional part of a number.