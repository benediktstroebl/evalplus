```python
def iscube(a):
    # Check if the number is greater than 0 and equals to a power of 3
    return (a > 0) and (a**(1/3) == round(a**(1/3)) )
```

This function checks if the number is greater than 0, and when raising the number to the power of 1/3 it equals the whole number. The use of the round function is to take care of the case of integers like 8 which would return a floating point number '2.0' when calculating 2**(1/3) and hence this case would fail the condition.