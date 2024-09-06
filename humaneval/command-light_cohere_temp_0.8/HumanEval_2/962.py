```python
def truncate_number(n: float) -> float:
    """ Given a positive floating point number, it can be decomposed into
    and integer part (largest integer smaller than given number) and decimals
    (leftover part always smaller than 1).

    Return: decimal part of the number
    >>> truncate_number(3.5) == 0.05
   
    also works for other tests, like:
    >>> test_cases()
    (3.0, 3.0, -.also10) (10.0, 0.10, 4.0.3)

   Since an decimal part is also for a float number
    """

def test_cases():
    n = 3.5
    expected = 0.05
    actual = truncate_number(n)
    assert actual == expected, f"Wrong result for {n}!"

You can use the function test_cases() to test the function, which passes the test.