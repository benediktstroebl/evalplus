```python
def truncate_number(number: float) -> float:
    return number - int(number)
```

The code directly exploits the definition of the problem statement: 'Return the decimal part of the number'. By subtracting the integer part of the number from the total number, we get the residual decimal part. 

For example, the integer part of 3.7 is 3, so truncate_number(3.7) returns 0.7. 

This solution is concise and elegant but assumes that the given number has an integer part. If the given number is a fraction like 3.125, the above method does not yield the expected result.