```python
def truncate_number(number: float) -> float:
    """
    Given a positive floating point number, returns the decimal part of the number.

    This function works by subtracting the integer part of the number from the number itself.

    :param number: A positive floating point number
    :return: The decimal part of the number
    """
    return number - int(number)


# Example usage:
print(truncate_number(3.5))  # Output: 0.5
print(truncate_number(10.99))  # Output: 0.99
print(truncate_number(5.0))  # Output: 0.0
```

In this script, the `truncate_number` function subtracts the integer part of the number (obtained by casting to `int`) from the number itself to return the decimal part. The example usage demonstrates how to use this function with different inputs.