
def circular_shift(x, shift):
    """Circular shift the digits of the integer x, shift the digits right by shift
    and return the result as a string.
    If shift > number of digits, return digits reversed.
    >>> circular_shift(12, 1)
    "21"
    >>> circular_shift(12, 2)
    "12"
    """

    # Circular shift the digits of the integer x, shift the digits right by shift
    # and return the result as a string.
    # If shift > number of digits, return digits reversed.

    # Base case
    if shift <= 0:
        return str(x)
    else:
        # Get the digits of x
        # Use a list comprehension to create a list of the digits of x
        digits = [int(d) for d in str(x)]

        # Get the last digit
        # Use the list comprehension to get the last digit
        # of x
        last_digit = digits[-1]

        # Shift the digits
        # Add a 0 to the beginning of the list
        digits.insert(0, 0)

        # Remove the last digit
        # Remove the last digit from the list
        digits.pop()

        # Get the last digit
        # Use the list comprehension to get the last digit
        # of x
        new_last_digit = digits[-1]

        # Get the rest of the digits
        # Use the list comprehension to get all but the last digit
        # of x
        rest_of_digits = digits[0:len(digits)-1]

        # Append the last digit
        # Use the list comprehension to append the last digit
        # of x
        rest_of_digits.append(last_digit)

        # Shift the digits
        # Remove the last digit
        rest_of_digits.pop()

        # Append the new last digit
        # Use the list comprehension to append the new last digit
        # of x
        rest_of_digits.append(new_last_digit)

        # Convert the digits to an integer
        # Convert the list to an integer
        x = int("".join(str(e) for e in rest_of_digits))

        # Recursive case
        # Circular shift the digits of x, shift the digits right by shift
        # and return the result as a string.
        # If shift > number of digits, return digits reversed.
        return circular_shift(x, shift - 1)


