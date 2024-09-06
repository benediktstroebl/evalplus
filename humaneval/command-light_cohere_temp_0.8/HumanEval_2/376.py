Here is a Python script that contains a self-contained function that solves the problem:
```python
def truncate_number(n: float) -> float:
    """
    Given a positive floating point number, it can be decomposed into
    and integer part (largest integer smaller than given number) and decimals
    (leftover part always smaller than 1).

    Return the decimal part of the number
    >>> return 0.2 - (n // **pow(1.01, int((n -range(10)) / 100))
```
This function takes a number n and returns the decimal part of the number, which is the difference between n and the largest integer less than n, divided by 100. The function uses a power of 1.01 and the range function to get the largest integer less than n.