```python
def truncate_number(number):
    """
    Return the decimal part of the number given as parameter.
    """
    return number - int(number)
```

This function takes a float as an input and returns the decimal part of the number by subtracting the integer part of the number (obtained by rounding down the input value) from the input number. The rounding-down process converts the float value to the nearest integer value, and the difference between the original number and the integer value gives the decimal part of the number. Finally, the function returns this decimal part of the number as the output. 

Here is a test case that can be used to validate the functionality of the function:
```python
test_case = [
    (3.5, 0.5),
    (2.5, 0.5),
    (1.1, 0.1),
    (12.345, 0.345)
]

for n, result in test_case:
    assert truncate_number(n) == result
``` 

The assert statement in the above test case compares the output of the `truncate_number` function with the expected output for each input number, ensuring the correct functionality of the function.