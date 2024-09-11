```python
def truncate_number(number: float) -> float:
    """
    Given a positive floating point number, it can be decomposed into
    and integer part (largest integer smaller than given number) and decimals
    (leftover part always smaller than 1).

    Return the decimal part of the number.

    :param number: A positive floating point number
    :return: The decimal part of the number
    """
    if number < 0:
        raise ValueError("Input number must be positive")
    
    # Calculate the decimal part by subtracting the integer part from the number
    decimal_part = number - int(number)
    
    return decimal_part

# Example usage
if __name__ == "__main__":
    print(truncate_number(3.5))  # Output: 0.5
```

In this code:

- We first check if the input number is negative and raise a `ValueError` if it is.
- We calculate the decimal part of the number by subtracting its integer part (`int(number)`) from the number itself.
- The decimal part is then returned.
- The `if __name__ == "__main__":` block is used to include an example usage of the `truncate_number` function.