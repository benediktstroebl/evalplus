
def circular_shift(x, shift):
    """Circular shift the digits of the integer x, shift the digits right by shift
    and return the result as a string.
    If shift > number of digits, return digits reversed.
    >>> circular_shift(12, 1)
    "21"
    >>> circular_shift(12, 2)
    "12"
    """
    # Initialise the new number of digits
    num_digits = x
    # Find the number of digits
    while num_digits > 10:
        num_digits /= 10
    # Find the remainder
    remainder = x % num_digits
    # Find the new number of digits
    new_num_digits = remainder + shift
    # Check if need to reverse the number
    if new_num_digits >= num_digits:
        # Reverse the number
        reverse = str(int(str(x)[::-1]))
        # Find the first digit of the reversed number
        first_digit = reverse[0]
        # Find the first digit of the reversed number
        second_digit = reverse[1]
        # Find the length of the reversed number
        reverse_length = len(reverse)
        # Length of the zero padded number
        pad = reverse_length - len(str(new_num_digits))
        first_pad = str(0) * pad
        second_half = str(int(second_digit) + int(first_pad))
        reverse_half = str(int(first_digit) + int(second_half))
        # Return the reversed number
        return reverse_half
    else:
        # Create a string of zeros
        zero_string = str(0) * (num_digits - new_num_digits)
        # Find the first and second digits
        first_digit = x / (10 ** (num_digits - 1))
        second_digit = x % (10 ** (num_digits - 1))
        # Find the first and second digits
        first_digit = str(int(first_digit))
        second_digit = str(int(second_digit))
        # Add the digits to the end of the zero string
        first_half = str(int(first_digit) + int(zero_string))
        second_half = str(int(second_digit) + int(first_half))
        # Return the number
        return second_half

