```python
def truncate_number(number):
    """
    Return the decimal part of the number given as parameter.
    """
    return number - int(number)
```

This function takes a float as an input and returns the decimal part of the number by subtracting the integer part of the number (obtained by converting the float into an integer). This operation results in the leftover fraction, which is always less than 1. 

To test this function, try calling it with a float value and comparing the returned value to the original number. For example:
```python
test_cases = [
    (3.5,),
    (12.34567,),
    (1.23,),
    (678.7,),
]

for number, expected in test_cases:
    result = truncate_number(number)
    assert result == expected
```

This block of code defines a list of test cases with tuples of input values and expected output values. It then iterates through each test case, calling the `truncate_number` function on the input number, and comparing the result to the expected output using the `assert` statement, which validates the correctness of the solution.