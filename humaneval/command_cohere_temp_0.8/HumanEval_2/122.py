```python
def truncate_number(number):
    return number - int(number)
```

The `truncate_number` function takes a float number as an argument, subtracts the closest integer to it (using `int()` to round the number), and returns the residual, which is the decimal part of the original number. 

Here is a simple test case to verify the functionality of the script:
```python
truncate_number(3.5) == 0.5
```

The result will be:
```bash
True
``` 

This proves that the function correctly returns the decimal part of the input number.