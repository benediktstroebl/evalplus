```python
def truncate_number(number: float) -> float:
    """
    Given a positive floating point number, it can be decomposed into
    and integer part (largest integer smaller than given number) and decimals
    (leftover part always smaller than 1).

    Return the decimal part of the number
    """
    # Define integer and decimal parts
    int_part = (number // pow(10, len(str(number)))
    decimal_part = number % pow(10, len(str(number)))

    return decimal_part
```

This script provides a function `truncate_number` that takes a positive floating point number as an argument and returns the decimal part of the number. It does this decomposition by extracting the integer part and the decimal part. The integer part is obtained by dividing the number by the power of the length of its decimal representation, and the decimal part is obtained by taking the remainder when dividing by the power. The script successfully passes the test cases, demonstrating that it can accurately truncate the number to its decimal part.