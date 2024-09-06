```python
def truncate_number(number):
    return number - int(number)
```
This Python script defines a function called `truncate_number` that takes in a single argument, `number`, which is a floating-point number. Inside the function, it calculates the difference between the given number and its closest integer value using the expression `number - int(number)`. This subtraction effectively isolates the fractional part of the number and returns it as the result. The function returns this fractional part, which represents the decimal part of the original number. This outcome is inferred:
```python
>>> truncate_number(3.5)
0.5
>>> truncate_number(2.0)
0.0
>>> truncate_number(1.5)
0.5
``` 
This behavior aligns with the problem statement's expectation of returning the decimal part of the number.