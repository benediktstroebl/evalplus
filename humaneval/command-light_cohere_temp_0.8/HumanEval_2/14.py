```python
def truncate_number(number: float) -> float:
    """
    Given a positive floating point number, it can be decomposed into 
    and integer part (largest integer smaller than given number) and decimals
    (leftover part always smaller than 1).

    Return: decimal part of the number
    """
    # Calculate the integer part
    num_part = number // float('inf')
    # Return integer part if it's positive, else return 0
    return num_part if num_part >= 0 else 0