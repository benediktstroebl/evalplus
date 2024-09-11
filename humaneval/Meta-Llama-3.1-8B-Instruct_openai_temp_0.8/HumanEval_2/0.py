### Truncating a Floating Point Number in Python
#### Problem Description
The goal is to write a Python function that takes a positive floating point number and returns the decimal part of that number. The decimal part is defined as the leftover part smaller than 1 after decomposing the input number into its integer part and decimals.

#### Solution

```python
def truncate_number(number: float) -> float:
    """
    Given a positive floating point number, it can be decomposed into
    an integer part (largest integer smaller than given number) and decimals
    (leftover part always smaller than 1).

    Return the decimal part of the number.

    Args:
    number (float): A positive floating point number.

    Returns:
    float: The decimal part of the input number.

    Example:
    >>> truncate_number(3.5)
    0.5
    """
    # Ensure the input is a positive number
    if number <= 0:
        raise ValueError("Input number must be positive.")
    
    # Decompose the number into its integer part and decimal part
    integer_part = int(number)
    decimal_part = number - integer_part
    
    # Return the decimal part
    return decimal_part
```

#### Explanation
This Python function uses simple arithmetic to decompose the input number into its integer part and decimal part. The integer part is obtained by converting the number to an integer, and the decimal part is calculated by subtracting the integer part from the original number. Finally, the decimal part is returned as the result.

#### Example Usage
You can test this function with the following code:

```python
print(truncate_number(3.5))  # Output: 0.5
print(truncate_number(10.7))  # Output: 0.7
```