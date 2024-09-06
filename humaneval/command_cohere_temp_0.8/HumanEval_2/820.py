```python
def truncate_number(number):
    """
    Return the decimal part of the number given as parameter.
    """
    return number - int(number)
```

This function takes a float as an input, `number`, and returns the decimal part of this number. It does so by taking the difference between the original number and the largest integer less than or equal to the number, effectively removing the integer part of the number and retaining only the decimal part. 

To verify the functionality, you can run the following cell in Python in the notebook or IDE:
```python
>>> truncate_number(3.5)
0.5
>>> truncate_number(1.5)
0.5
>>> truncate_number(2.0)
0
>>> truncate_number(11.3)
0.3
```

This should return the decimal part of the provided number, consistent with the example provided in the problem description.