```python
def truncate_number(number):
    """
    Return the decimal part of the number given as parameter.
    """
    return number - int(number)
```
This function simply converts the parameter to an integer (rounded down), and then subtracts this integer from the original number - this effectively leaves only the decimal part. 

To test this, you can call this function with the input values of 3.5, and it will return 0.5.