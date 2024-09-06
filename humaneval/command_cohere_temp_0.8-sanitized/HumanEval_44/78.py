def change_base(x, base):
    return str(x)
    # Use string format to convert to base, ensure subtraction doesn't raise error
    format_str = '{{0:b{}}}'.format(base)
    return format_str.format(x)