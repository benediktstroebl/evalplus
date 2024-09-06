```python
def truncate_number(number):
    """
    Return the decimal part of the number given as parameter.
    """
    return number - int(number)
```

This function takes a float as an input, `number`, and returns the decimal part of the number by subtracting the integer part of the number, obtained by converting the float to an integer (using `int()`), from the input number. This operation effectively separates the decimal part and returns it as the result. 

To test this function, you can call it with a floating-point number to see the result. For example:
```python
result = truncate_number(3.5)
print(result)  # Output: 0.5
```

This will print the decimal part of the input number (3.5), which is 0.5. 

Such a function can be used in various applications where you need to work with decimal parts of numbers, such as calculating discounts, taxes, or interest in financial applications. 

If you are working with Python 3, you could use the `round()` function to achieve the same result in a more concise way:
```python
def truncate_number(number):
    return round(number*1.)
```

In this version, `round()` is used to round the number to the nearest whole number, and then `*1.</` is used to get the decimal part of the number, as `round()` returns the result as an integer, and then the result is converted to a float.