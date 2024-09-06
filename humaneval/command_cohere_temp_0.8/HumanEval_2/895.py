```python
def truncate_number(number: float) -> float:
    return number - int(number)
```

This function simply computes the difference between the input number and the nearest integer, which represents the decimal part of the number. 

To test this function, you can call it with a floating point input and compare the result to the expected value. 
For example:
```python
truncate_number(3.5) == 0.5
```

The result should be True, confirming that the function behaves as expected. 

This approach is efficient and suitable for a variety of inputs, regardless of the complexity of the number.