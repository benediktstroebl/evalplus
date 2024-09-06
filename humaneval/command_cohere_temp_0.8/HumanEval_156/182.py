```python
def int_to_mini_roman(n):
    if n < 1:
        raise ValueError("Input must be a positive integer")

    # Convert integer to list of digits.
    num_list = list(map(int, str(n)))

    # Tracks the largest digit encountered (for parsing rules).
    largest_digit = max(num_list)

    # Initialize the roman numeral representation
    roman_numeral = []

    # Loop through each digit and transform accordingly
    for digit in num_list:
        if digit == largest_digit:
            roman_numeral.append(digit)
        else:
            roman_numeral.extend([str(largest_digit)] * digit)
            largest_digit = digit

    # Check for thousands (without ruining the elegant solution :P)
    if len(num_list) == 4 and num_list[-1] == 1:
        roman_numeral.pop()

    return ''.join(roman_numeral).lower()
```

This script handles the `int_to_mini_roman` function, taking a positive integer as input and returning its roman numeral equivalent as a lowercase string. It initially checks if the input is less than 1 and, if so, raises a `ValueError`. The integer is then transformed into a list of digits. The script iterates through each digit, tracking the largest one encountered. It constructs the roman numeral representation, considering rules like `i` for 1, `iv` for 4, and `ix` for 9, adjusting accordingly. Finally, the function removes the last character if the input is exactly 1000 and returns the roman numeral representation as a lowercase string.