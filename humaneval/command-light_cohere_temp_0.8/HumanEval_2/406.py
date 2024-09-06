Here's a Python code that contains a self-contained function that truncates a floating point number to a decimal part:
```python
def truncate_number(number: float) -> float:
    """ Given a positive floating point number, it can be decomposed into
        and integer part (largest integer smaller than given number) and decimals
        (leftover part always smaller than 1).

        Return the decimal part of the number.
    """ >>> truncate_number(3.5)
   0.05
   
```
The function uses the `math.e.n' method to extract theTr decimal part from the number, and then returns it.