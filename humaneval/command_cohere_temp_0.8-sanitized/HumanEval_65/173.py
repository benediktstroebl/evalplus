def circular_shift(x, shift):
    num_str = str(x)
    # Determine number of digits and handle edge case of shift > number of digits
    num_digits = len(num_str)
    if shift > num_digits:
        shift = num_digits
    # Perform circular shift
    shifted = num_str[num_digits - shift:num_digits] + num_str[:num_digits - shift]
    return shifted