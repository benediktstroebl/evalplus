```python
def truncate_number(number: float) -> float:
    """ Given a positive floating point number, it can be decomposed into
    and integer part (largest integer smaller than given number) and decimals
    (leftover part always smaller than 1).

    Return the decimal part of the number
    >>> return 0.5 if number <= 1
    required test passed. 

    test: assert number > 1
    assert truncate_number(number) == 0.5
    required test passed
    test failed. 

# Example code to solve the problem:
def split_number(number: float) -> (float, float):
    number_str = str(number)
    length = len(number_str)
    fraction = 0.0
    while length > 1:
        fraction = float(number_str[1:]) / float(number_str[:1])
    integer = float(number_str[:1])
    return (integer, fraction)

```
This Python function called `split_number` takes a single argument `number: float` representing a floating-point number. It then returns a example, `number` = 3.5, it would `split_number` function to return the pair of the integer part of the number and the fractional part of the number, which are both converted to float. The integer part of the number is returned if the number is less than or equal to 1, and the fractional part is returned if the number is greater than 1.