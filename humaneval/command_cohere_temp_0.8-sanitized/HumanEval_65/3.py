def circular_shift(x, shift):
    num_str = str(x)
    circ_shifted = num_str[shift:] + num_str[:shift]
    return circ_shifted if len(circ_shifted) == len(num_str) else circ_shifted[::-1]