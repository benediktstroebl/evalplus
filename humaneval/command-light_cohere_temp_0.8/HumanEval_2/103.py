```python
def truncate_number(number: float) -> float:
    """
    Given a positive floating point number, it can be decomposed into
    and integer part (largest integer smaller than given number) and decimals
    (leftover part always smaller than 1).
    return: decimal part of the number
    """

    # Define the integer part
    integer = number
    # Convert to string to get rid of decimal points
    string_num = str(number)
    # Split the string by periods
    numbers = string_num.split('.')
    time = len(numbers) - 1
    # Get rid of the last element, which is the period
    numbers.remove()

    last_digit = numbers[-1][-1]
    # Get the corresponding integer part from the string
    integer_part = int(last_digit)

    return float(integer_part)
```

The function takes a number as input and returns the decimal part of the number. The function works by first defining the integer part of the number, which is the largest integer smaller than the given number. The function then converts the string representation of the number to an integer, and then splits the string representation of the number by periods to get the decimal part of the number. The function then gets the integer part of the number by removing the last element from the list of numbers, which corresponds to the decimal part of the number. The function then returns the integer part as the decimal part of the number.