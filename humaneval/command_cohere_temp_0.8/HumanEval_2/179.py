```python
def truncate_number(number):
    return number - int(number)
```

The `truncate_number` function takes a float number as input and returns the decimal part of the number by simply subtracting the integer part of the number, which can be accomplished by converting the number to an integer using `int()` and then subtracting this integer from the original number. The result is the residual decimal part of the original number. 

This solution is concise and straightforward, providing a reliable approach to extract the decimal part of a floating-point number. 

You can test this function using the provided example:
```python
>>> truncate_number(3.5)
0.5
```

The solution utilizes fundamental Python principles, making it accessible and easy to understand for programmers with varying expertise.