```python
def truncate_number(number):
    return number - int(number)
```

The `truncate_number` function takes a single parameter, `number`, which represents the positive floating point number to be decomposed into an integer part and a decimal part. It does this by subtracting the nearest integer (rounded down) of the number from the original number. This subtraction effectively captures only the leftover fraction, which is necessarily smaller than one. The result of this operation is the desired decimal part of the number, which is then returned by the function. 

This approach utilizes the trait of floating-point numbers that allows them to be accurately represented as a sum of an integer and a fraction.

To test this script, you can call the `truncate_number` function with a floating-point input, and the returned value should be the decimal part of the input. For example:
```python
assert truncate_number(3.5) == 0.5
assert truncate_number(2.0) == 0.0
```

This would verify the correctness of the implementation.