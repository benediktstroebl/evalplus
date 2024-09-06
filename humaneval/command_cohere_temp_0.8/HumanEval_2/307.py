```python
def truncate_number(number):
    return number - int(number)
```

The `truncate_number` function takes a positive floating point number as input and returns the decimal part of the number. It does so by taking the difference between the given number and the nearest integer (rounded down) represented by the number, which effectively removes the integer part of the decomposition and leaves behind the decimal part. 

Here is an example usage of the function:
```python
>>> truncate_number(3.5)
0.5
>>> truncate_number(12.34567)
0.34567
```

This function is a straightforward and effective solution, providing a clear and concise implementation that achieves the intended functionality as stated in the problem description. It is important to note that this function assumes that the input number is a positive floating point number, and it may not work as expected for other types of input.