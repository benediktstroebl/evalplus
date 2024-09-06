```python
def multiply(a, b):
    """Returns the product of the unit digits of the inputted integers."""
    return int(str(a)[-1]) * int(str(b)[-1])
```
The above function extracts the last digit of the strings representation of each number, multiplies them, and returns the resulting integer. 

The extraction is performed using Python's slice notation where [-1] indicates the last index of the string. Trying this example:
```python
multiply(12, 3)
```
Would result in the following output:
```
3
``` 

As explained above, this is due to the last digits of 12 and 3 being 6 and 3 respectively, and 63 being their product.