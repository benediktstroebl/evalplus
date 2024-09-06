```python
def truncate_number(number: float) -> float:
    return number - int(number)
```
This function simply computes the difference between the given floating point number and the nearest integer, which represents the residual decimal part of the original number. 

To test this script, you can call the function with a floating point input, and the result will be the decimal part of the input. For example:
```python
print(truncate_number(3.5))  # Expected output: 0.5
```
The script assumes that the given number is positive, which is the context provided in the problem statement. If negative numbers are also considered, the script would need adjustments to handle those cases respectively.