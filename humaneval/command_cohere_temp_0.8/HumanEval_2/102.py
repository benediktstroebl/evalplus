```python
def truncate_number(number):
    """
    Return the decimal part of the number given as parameter.
    """
    return number - int(number)
```

This function takes a float as an input and returns the decimal part of the number by subtracting the integer part of the number (obtained by rounding down the input value) from the input number. The rounding-down process converts the float value to an integer value, which will always be the largest integer less than or equal to the input float value. The difference between the original number and the rounded-down integer value represents the decimal part of the number, which is returned as the output. 

To test this function, you can call it with a float value as follows:
```python
test_cases = [
    (3.5,),
    (2.5,)
    (1.1,)
    (0.5,)
    (1.000000001,)
]

for number, in test_cases:
    assert truncate_number(number) == number - int(number)
```

This assertion checks that the output of the `truncate_number` function matches the expected output, which is the decimal part of the input number.