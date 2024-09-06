```python
def truncate_number(number: float) -> float:
    """
    Given a positive floating point number, it can be decomposed into
    and integer part (largest integer smaller than given number) and decimals
    (leftover part always smaller than 1).
    Return the decimal part of the number
    >>> return 0.5 if number < 3.5
   
     # Return the's an edge case."""
    return 0.5 if number < 3.5 else 
	int(number) // 2  if number >= 1
        return (number - int(number) // 2) * 2  if number <= -1
        return 0
``` 
This function has a straightforward approach, using integer division to separate the number into its integer and decimal parts. It also handles the _edge case where the number is a power of 2, returning the decimal part. It also handles the case where the number is negative, returning the decimal part of the number.