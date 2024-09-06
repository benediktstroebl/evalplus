```python
def truncate_number(number):
    return number - int(number)
```

The provided Python script defines a function `truncate_number` that takes a single argument, `number`, which is expected to be a positive floating point number. The purpose of this function is to return the decimal part of the input number. This is achieved by subtracting the nearest integer (rounded down) from the input number. This integer part represents the largest integer less than or equal to the input number, and the remainder becomes the decimal part, which is always less than 1. 

For example, if the input is `3.5`, the function will return `0.5`, as `3` is the largest integer less than or than `3.5`, and subtracting `3` from `3.5` gives us `0.5`.

The script assumes that the input number is valid and adheres to the problem statement's requirements, specifically that it is a positive floating point number.