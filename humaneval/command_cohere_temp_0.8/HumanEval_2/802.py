```python
def truncate_number(number):
    return number - int(number)
```

The `truncate_number` function takes a positive floating point number as input and returns the decimal part of the number. It does so by taking the difference between the given number and the largest integer less than or equal to the number, which is achieved by converting the floating point number to an integer using `int()`, effectively truncating the number to the nearest integer. The leftover part, which is less than one, represents the decimal part that was removed from the original number. 

Here is an example usage of the function:
```python
>>> truncate_number(3.5)
0.5
>>> truncate_number(2.0)
0.0
```

This script accurately solves the problem using an efficient and concise approach. It provides a clear and direct implementation of the specification provided in the prompt, thus meeting the requirement for a self-contained solution.