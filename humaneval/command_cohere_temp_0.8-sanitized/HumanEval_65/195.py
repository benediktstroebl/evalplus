def circular_shift(x, shift):
    num_str = str(x)
    num_list = list(num_str)
    if shift > len(num_list):
        shift = shift % len(num_list) 
    num_list[:shift], *num_list[shift:] = *num_list[shift:], num_list[:shift]
    return "".join(num_list)