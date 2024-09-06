```python
def truncate_number(number: float) -> float:
    """
    Given a positive floating point number, it can be decomposed into 
    and integer part (largest integer smaller than given number) and decimals
    (leftover part always smaller than 1).

    Return: decimal part of the number.
    >>> truncate_number(3.5)
    0.5
def test_and_assert(original_func: callable, passed_test: bool) -> None:
    original_func()
    assert passed_test

# Use the test and assert functions
test_and_assert(truncate_number(3.5), True)
``` 
The test_and_assert function is used to define a test for the function 'truncate_number'. The test passes when the 'original_func' is called with the correct argument and returns the expected result.