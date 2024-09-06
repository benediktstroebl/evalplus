```python
def truncate_number(number: float) -> float:
    return number - int(number)
```

This function simply computes the difference between the input number and the nearest integer, which represents the residual decimal part of the original number. 

To test this script, you can call the function with a floating-point input and verify that the output is the expected decimal part. 

For example:
```python
truncate_number(3.5)  # Expected output: 0.5
``` 
This would indeed return 0.5, which is the decimal part of the number 3.5. 

If you wish to test other numbers, you can incorporate them into the test code section provided above.