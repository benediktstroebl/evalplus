```python
def truncate_number(number):
    return number - int(number)
```

The `truncate_number` function takes a single argument, `number`, which is expected to be a positive floating point number. It returns the decimal part of the number by subtracting the integer part of it. The integer part of a number is the largest integer that is less than or equal to the given number. 

For example, given the prompt's example, `truncate_number(3.5)` is evaluated to `0.5`, since `3` is the integer part of `3.5`, and taking that away from `3.5` leaves us with `0.5`.