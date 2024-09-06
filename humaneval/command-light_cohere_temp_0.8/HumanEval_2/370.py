```python
def truncate_number(number: float) -> float:
    """ Given a positive floating point number, it can be decomposed into
    and integer part (largest integer smaller than given number) and decimals
    (leftover part always smaller than 1).

    Return: The decimal part of the number.
    number % 1000 = remainder after dividing number by 1000.
    return :int(floor(number % 1000))
    """

    # Test Case 1
    assert truncate_number(3.5) == 0.5 and
    time: floor(3.5 % 1000) = 0

    # Test Case 2
    assert truncate_number(-3.5) == -1.9

    time: floor(-3.5 % 1000) = 1

    # Test Case 3
    assert truncate_number(1.25e) == 0.05

    time: floor(1.25 % 1000) = 0.05

    time: 0.01 is an integer part. 

   assert truncate_number(10300.2) == 0.99.2

    time: floor(10300.2 % 1000) = 0.02

    assert truncate_number(3.5) == 0.000 all teststime correct tests for truncate_number.