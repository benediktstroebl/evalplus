def circular_shift(x, shift):
    num_digits = len(str(x))
    shifted_digits = list(str(x))
    if shift > num_digits:
        shift = num_digits
    for _ in range(shift):
        del shifted_digits[0]
    shifted_digits.append(shifted_digits[0])
    return ''.join(shifted_digits)