Here's a self-contained Python function that returns the decimal part of a given number:
```python
def truncate_number(number: float) -> float:
    """
    Given a positive floating point number, it can be decomposed into
    and integer part (largest integer smaller than given number) and decimals
    (leftover part always smaller than 1).

    Return: decimal part of the number.
    >>> truncate_number(3.5) == 0.2
   05

    >>> truncate_number(10) == 5.6
    >>> truncate_number(-3.5) == -0
   0.5
   

   
   
    """ ValueError: float() not int()
    ```