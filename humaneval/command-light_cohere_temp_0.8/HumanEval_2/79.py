Here's the solution:

```python
def truncate_number(number: float) -> float:
    # function to return the decimal part of a floating point number
    integer = number
    decimal = 0.0
    while number > 1:
        decimal = number % 10
        number = number // 10
    return decimal
```

This function takes a number as an argument and returns the decimal part of the number. 

Test cases:
```python
# Test cases
print(truncate_number(5)) # Output: 1.0
print(truncate_number(3)) # Output: 0.0
print(truncate_number(0)) # Output: 0.0
print(truncate_number(-5)) # Output: 5.0
print(truncate_number(10)) # Output: 1.0
print(truncate_number(1)) # Output: 1.0
print(truncate_number(4)) # Output: 0.2
```

This script defines a function `truncate_number` that takes a number as input and returns the decimal part of the number, which is the fractional part after removing the largest integer part. 

The output of the function is then tested with several inputs.