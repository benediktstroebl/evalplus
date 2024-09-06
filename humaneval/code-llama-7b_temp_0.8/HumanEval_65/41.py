
def circular_shift(x, shift):
    """Circular shift the digits of the integer x, shift the digits right by shift
    and return the result as a string.
    If shift > number of digits, return digits reversed.
    >>> circular_shift(12, 1)
    "21"
    >>> circular_shift(12, 2)
    "12"
    """
    # Base case
    if x == 0 or shift == 0:
        return str(x)

    # Divide the number in two halves
    # First half contains the digits before the last digit
    # Second half contains the digits after the first digit
    first_half = x // 10
    last_digit = x % 10
    second_half = x // 100 * 10 + last_digit

    # Recursive call
    first_half_string = circular_shift(first_half, shift - 1)
    second_half_string = circular_shift(second_half, shift - 1)

    # Last digit should be inserted at position (shift - 1)
    # If shift is more than the number of digits, insert it at the beginning
    return first_half_string[-(shift % len(first_half_string)):] + \
        str(last_digit) + \
        second_half_string[:-(shift % len(second_half_string))]

