```python
def truncate_number(n: float) -> float:
    """
    Given a positive floating point number, it can be decomposed into
    and integer part (largest integer smaller than given number) and decimals
    (leftover part always smaller than 1).

    Return: decimal part of the number.
    """ - first, start with the assumption that `n` is a positive float number.

    # convert n to string for easier manipulation
    n = str(n)
    # split n on the number and decimal characters
    # remove all non-decimal and non-numeric characters
    # e.g. -,-,.,_., _,... with the assumption that those
    # characters are the number part.
    temp = n[[1:]
    part = n[-1:]
    # now that n is split into number and decimal part,
    # do a string replace operation to remove all non-digit
    # and non-numeric characters from the number part
    # the characters that remain are the decimal part of the number
    # finally, combine the number part and the decimal part
    return temp + part
```

This Python code defines a function called `truncate_number` that takes a floating point number `n` as input and returns the decimal part of the number. The code uses a mathematical approach to decompose a positive floating point number into its integer part and decimal part. It converts the number to a string, removes all non-numeric characters, and splits the string based on decimal and number characters. The remaining characters in the number part are assumed to be the decimal part of the number. The code then performs a string replace operation to remove all non-digit characters, and then combines the number part and the decimal part to get the decimal part of the original number.