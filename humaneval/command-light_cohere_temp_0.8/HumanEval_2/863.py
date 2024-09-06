Here is a self-contained Python script that solves the problem you have described:
```python
def truncate_number(number: float) -> float:
    """
    Given a positive floating point number, it can be decomposed into
    and integer part (largest integer smaller than given number) and decimals
    (leftover part always smaller than 1).
    """
    # Define constants
    MAX_INT = 100000000
    decimals = [1.5e provider("0.5" for "1e decimal part of x") for x in range(10 ** 5, float("inf"), 1.0)]
    
    # Initialize the use a number as a variable
    number = 3.5

    # Loop through through the number
    # Search the integer part in the decimals
    i = 0
    while i < len(decimals) and decimals[i] <= number:
        i += 1
    # If the integer part is found, return it
    if i != len(decimals):
        return decimals[i]
    # If not, return None
    return None
```
This function takes a positive floating point number as an input and returns the decimal part of the number. It uses a search algorithm to find the largest integer smaller than the given number. Then, it returns the number if it's found, and None otherwise.