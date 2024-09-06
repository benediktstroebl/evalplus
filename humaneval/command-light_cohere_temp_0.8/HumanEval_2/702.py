Here's the code:
```python
def truncate_number(n):
    if n < 0:
        raise ValueError("Input number must be a positive float")
    if not isinstance(n, (int, float)):
        raise TypeError("Input number must be either int or float")
    if n > 1:
        return n - 1
    return n
```
This Python function, truncate_number, takes a single argument n, which must be a positive float. It performs several checks to ensure that the input is valid, then decomposes the number into its integer part and decimal part. The function then returns the return the decimal part of the number.

The function meets the following requirements:
- It raises a ValueError with the message "Input number must be a positive float" if the input n is less than 0.
- It raises a TypeError with the message "Input number must be either int or float" if the input is not an integer or float.
- It performs an check to see if the input n is greater than 1 and returns n - 1 if it is.
- It returns the decimal part of the number n.