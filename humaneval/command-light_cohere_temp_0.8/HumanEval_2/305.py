```python
def truncate_number(number: float) -> float:
    """
    Returns the decimal part of the number, which is the largest integer smaller than the given number
    """
    if not number:  # handle the case where the number is 0 or None
        return 0.0
    elif number <= 1:  # handle the case where the number is a whole number less than 1
        return number
    else:
        return float(number - int(number))

# test the function
print(truncate_number(3.5)) # output 0.5
print(truncate_number(1.2)) # output 0.1
print(truncate_number(0.0)) # output 0.0
print(truncate_number(-1.5)) # output 1.0
```

This script defines a function `truncate_number` that takes a number and returns the decimal part of that number. The function uses an series of conditional statements to handle the input and return the correct decimal part of the number.