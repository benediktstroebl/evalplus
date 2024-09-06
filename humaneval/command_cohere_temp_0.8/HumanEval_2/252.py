```python
def truncate_number(number):
    return number - int(number)
```

The `truncate_number` function takes a positive floating point number as input and returns the decimal part of the number. It does so by taking the difference between the given number and the closest integer (biggest whole number smaller than the given number). This difference is the desired decimal part of the original number. 

Here are some examples of how the function behaves on different inputs:
```
>> truncate_number(3.5)
0.5
>> truncate_number(10.99)
0.99
>> truncate_number(2.0)
0.0
``` 

The function returns the decimal part of the number, as described in the problem statement. 

This solution is straightforward and effective, but it may be vulnerable to potential issues with floating-point precision in certain programming environments. Although not explicitly required in the problem statement, the function assumes that the input number is a positive floating-point number.