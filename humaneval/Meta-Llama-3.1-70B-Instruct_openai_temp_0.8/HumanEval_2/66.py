```python
def truncate_number(number: float) -> float:
    """
    Given a positive floating point number, it can be decomposed into 
    and integer part (largest integer smaller than given number) and decimals 
    (leftover part always smaller than 1).

    Return the decimal part of the number.

    >>> truncate_number(3.5)
    0.5
    """
    return number - int(number)


# Example usage:
if __name__ == "__main__":
    print(truncate_number(3.5))  # Output: 0.5
    print(truncate_number(10.8))  # Output: 0.8
    print(truncate_number(0.7))  # Output: 0.7
```
This script defines a function `truncate_number` that takes a positive floating point number and returns its decimal part. The function works by subtracting the integer part (obtained by converting the number to an integer) from the original number. The result is the decimal part. The script includes example usage in the `if __name__ == "__main__":` block.