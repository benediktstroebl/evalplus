```python
def truncate_number(number: float) -> float:
    return round(number) // 1 if number > 1 else number

# Test cases
assertEqual(truncate_number(3.5), "0.2" )
 assertEqual(truncate_number(1.0), "0.0") )
 assertEqual(truncate_number(-3.5), "0.2") )
 assertEqual(truncate_number(0.5), "0.0") )
 assertEqual(truncate_number(1), "1") 
``` 
This Python code defines a function `truncate_number` that computes the integer part of a given number, truncating decimals if the original number is greater than 1. It takes advantage of the Python's built-in `round()` function to round the number to the nearest integer and then divides by 1 to retrieve the decimal part of the number.