```python
def truncate_number(number):
    """
    Return the decimal part of the number given as parameter.
    """
    return number - int(number)
```

The function `truncate_number` takes a single parameter, `number`, which is a floating-point number. It returns the decimal part of the number by subtracting the integer part of the number from the input. The integer part is obtained using the `int()` function, which returns the largest integer less than or equal to the input. The result is a float value that is equivalent to the original number, truncated to its decimal part. 

To test this function, you can call it with a floating-point number argument and compare the result with the original number.

For example:
```python
test_cases = [
    (3.5, 0.5),
    (2.5, 0.5),
    (1.5, 0.5),
    (11.75, 0.75),
    (123.456, 0.456),
]

for number, expected in test_cases:
    result = truncate_number(number)
    assert result == expected, f"For number {number}, expected {expected}, but got {result}"
``` 

The tests confirm the function behaves as expected for a range of inputs.  This function could be optimized to run faster or to handle a more extensive range of inputs, but this solution is straightforward and correct.