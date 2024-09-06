```python
def truncate_number(number):
    return number - int(number)
```

The `truncate_number` function takes a positive floating point number as input and returns the decimal part of the number. It does so by taking the difference between the given number and the nearest integer (largest integer less than the number), which is achieved by flooring the number to the nearest integer (`int(number)`), and the result is the residual fractional part of the original number. 

Here are some example outputs when the function is called with different input values:
```
- truncate_number(3.5) -> 0.5
- truncate_number(7.7) -> 0.7
- truncate_number(12.12) -> 0.12
``` 
This script solves the given problem statement, which is to return the decimal part of the original number. 

If you would like to see additional examples or have more questions about the logic involved, let me know!