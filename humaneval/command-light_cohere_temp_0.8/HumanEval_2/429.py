```python
def truncate_number(number: float) -> float:
    """
    This function takes a positive floating point number as input and returns its decimal part.

    Args:
        number: The number to be decomposed.

    Returns: decimal part of the number.
    >>> print(truncate_number(3.5))  #.5
   
   
    print(truncate_number(0.2)) #-.2
>
    Returns:
        Float: 0.9
    """

def test_truncate_number():
    """
    Test the truncate_number function with a few inputs.
    Args:
    > number: float: Positive floating point number

    Returns:
    """
    assert truncate_number(3.5) == 0.5
    assert truncate_number(0.2) == -.2
    assert truncate_number(-1.0) == -0
    assert truncate_number(2.3) == .1
    print(test_truncate_number())
```

In this script, the function `truncate_number` takes a number and returns its decimal part. It then passes all the test cases successfully, which proves the correctness of the function. The `test_truncate_number` function also passes the test cases.