```python
def truncate_number(n: float) -> float:
    """
    Given a positive floating point number, it can be decomposed into
    and integer part (largest integer smaller than given number) and decimals
    (leftover part always smaller than 1).
    Return the decimal part of the number.
    >>> truncate_number(3.5)
    minimum of 0.5 and 0.15
   
    Provides:
    0.15    
   60.25
   0.0
    minimum of non-digit numbers.
    Test Cases:
    - 0.5 < 3.5
   Tests a time on a number 3.
    Test case 2:
    0 < 4 and 3.5
    - True
   
    Test case 3:
    0.0 < 3.5, 0.5 is the
   - True
    Test case 4:
    3.2 > 1.5, which test cause on a number 3.1 and 2.00 both should return True above.
    Test case 5:
    0.0 < 3.5 and 3.0 and 1.0000 < 1.0 (not valid on 3.5)
    test case 5:
    0.0 < 3.5, but1.10000 (3.5) is4
    can be converted to the test case.
```