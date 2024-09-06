```python
def truncate_number(n): 
    # Use python's built-in floor division to get the largest integer part of the number
    i = n // 1
    # Use the floor division to get the decimal part of the number
    d = n % 1 
    return d
``` 
This Python code defines a function `truncate_number` that takes a floating-point number `n` as input and returns the decimal part of the number. The function uses the floor division to separate the number into its integer part and decimal part. The function then returns the floor division result, which is the largest integer smaller than the input number. The function performs the floor division, which means that it returns the largest integer that is less than the input number, leaving the remainder as the decimal part.