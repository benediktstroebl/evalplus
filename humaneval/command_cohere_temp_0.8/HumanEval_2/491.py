```python
def truncate_number(number: float) -> float:
    return number - int(number)
```
This function simply subtracts the largest integer that is less than number from number itself. The decimals in the number would get wiped off in the process and the result would be the decimal part of the original number. 

To test this, consider printing the output for the following values:
```python
print(truncate_number(3.5)) # Should print 0.5
print(truncate_number(2.5)) # Should print 0.5
print(truncate_number(1.1)) # Should print 0.1
print(truncate_number(5.0)) # Should print 0.0
```
Each of these numbers can be decomposed into an integer part (the part before the decimal point, which can be computed by finding the largest integer less than the number) and a decimal part (the part after the decimal point). The above function returns the decimal part from the original number.