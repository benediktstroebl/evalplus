```python
def truncate_number(number):
    return number - int(number)
```
This Python script defines a function called `truncate_number` that takes in a single argument, `number`, which is a floating-point number. Inside the function, it calculates the difference between the given number and its closest integer value using the `int()` function, which effectively removes the integer part of the number. The result is returned as the residual decimal part of the original number. This operation is useful when you want to focus on the decimal portion of a floating-point value while discarding the integer portion.