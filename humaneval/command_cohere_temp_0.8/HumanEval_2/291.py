```python
def truncate_number(number):
    return number - int(number)
```

The function takes in a `number` as its input, which is a positive floating point number, and returns the decimal part of the number. It achieves this by taking the difference between the given number and the closest integer value represented by the number. This difference is the residual decimal part of the original number. 

Here is an example usage of the code:
```python
>>> truncate_number(3.5)
0.5
>>> truncate_number(2.0)
0.0
```

This demonstrates the function's ability to isolate and return the decimal part of a floating-point number, which is achieved through a simple mathematical operation that retains the original decimal value.