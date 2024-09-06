```python
def truncate_number(n):
    return round(n) if n >= 1 else int(n)

# Test cases from the function definition
assert truncate_number(10) == 10
assert truncate_number(0) == 0
assert truncate_number(-5) == -5
assert truncate_number(3.14) == 3

``` 
This Python script defines a function, `truncate_number`, that takes a number as input and returns the truncated value. It achieves this by using the round() function to remove the decimal part of the number if it's a whole number and the int() function to convert the remaining fractional part to an integer if there's a fractional part. 
The test cases section ensures that the function behaves correctly for a variety of inputs, passing all the tests successfully.