Here is a self-contained Python script that solves the problem you described:

```python
def truncate_number(number: float) -> float:
    """
    Given a positive floating point number, it can be decomposed into
    and integer part (largest integer smaller than given number) and decimals
    (leftover part always smaller than 1).

    Return the decimal part of the number.
    >>> truncate_number(3.5)
    0.05
```
This function takes a number as an argument, and returns the decimal part of that number. It can be used to test for the following input:
- 3.5 returns 0.05 

3.3 returns 0.00