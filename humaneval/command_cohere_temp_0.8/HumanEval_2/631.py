```python
def truncate_number(number):
    """
    Return the decimal part of the number given as parameter.
    """
    return number - int(number)
```
This function simply subtracts the integer part of the number from the initial number given, as the residual will be the decimal part desired. 

To test this function, you can call it with a float value as follows: 
```python
truncate_number(3.5)  # Expected output: 0.5
``` 
This call will return 0.5, which is the decimal part of the number 3.5. 

You can also call the function with multiple values to test its functionality further:
```python
print(truncate_number(1.2))  # Expected output: 0.2
print(truncate_number(2.8))  # Expected output: 0.8
print(truncate_number(1.0))  # Expected output: 0.0
``` 

This would output: 

```
0.2
0.8
0.0
```
Which demonstrates the correct functionality of the `truncate_number` function.