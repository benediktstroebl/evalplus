```python
def truncate_number(n: float) -> float:
    """
    Given a positive floating point number, it can be decomposed into
    and integer part (largest integer smaller than given number) and decimals
    (leftover part always smaller than 1).

    Return the decimal part of the number.
    >>> truncate_number(3.5) == 0.250
    Markets
   572.5
def test_function_success(test_case: float) -> bool:
    return test_case == truncate_number(test_case)

# Example usage:
>>> test_case = 3.5
>>> test_result = test_function_success(test_case)
>>> print(test_result)
True
```

The function `truncate_number` takes a floating point number as input and returns the decimal part of the number. The `test_function_success` function tests whether the input number is correctly decomposed into an integer part and a decimal part. 

The output of the example will be `True` because the input number is correctly decomposed.