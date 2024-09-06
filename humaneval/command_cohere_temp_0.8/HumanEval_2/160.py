```python
def truncate_number(number):
    return number - int(number)
```
This function simply subtracts the integer part of the number from the original number, which equals the decimal part, as described in the problem statement. The function int(number) extracts the largest integer part of number, and subtracting it from the original number yields the remaining fraction.