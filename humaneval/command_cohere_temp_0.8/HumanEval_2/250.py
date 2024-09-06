```python
def truncate_number(number):
    return number - int(number)
```

The `truncate_number` function takes a positive floating point number as input and returns the decimal part of the number. It does so by taking the difference between the given number and the closest integer (floor value). For example, `truncate_number(3.5)` returns `0.5`, as 3 is the largest integer less than 3.5 and the difference between them is 0.5. 

This solution relies on some basic principles of floating-point numbers in Python:
- A floating-point number in Python represents an approximation of a real number.
- Python represents floating-point numbers as a tuple of two values—mantissa and base exponent.
- The mantissa is a tuple of integers, where the first integer represents the significant figures, and the second integer represents the base exponent.
- Python represents the floating-point numbers closely adhering to the IEEE 754 standard.

This approach is concise and operates on the given number directly, utilizing the inherent nature of floating-point representation in Python. 

Note that this solution assumes that the input number is a positive floating-point number. If the number is negative or contains multiple decimal places, the output will be interpreted as the decimal part of the number but may not yield the expected result. In such cases, additional parsing and handling may be necessary.