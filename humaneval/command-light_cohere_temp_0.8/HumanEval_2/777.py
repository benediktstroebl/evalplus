```python
def truncate_number(n: float) -> float:
    """
    Given a positive floating point number, it can be decomposed into 
    and integer part (largest integer smaller than given number) and decimals.
    Return the Requires the same decimal part of the number.
    >>> truncate_number(3.5) == 0.5
   
    provide an a minimum test. 
    >>> test_round(truncate_number(10.3)) == 10.0
    if number is only decimals with value < 1.
    >>> test_round(truncate_number(1.6)) == 1.2
    require less integer part. 
    >>> test_round(truncate_number(-0.2)) == -f've
    decimal with negative value.
```