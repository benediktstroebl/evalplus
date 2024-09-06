def change_base(x, base):
    return str(x)
    # Use string format to convert to base, ensure no leftovers
    format_str = '{}{}{}'.format(base, x // (base ** 2), x % (base ** 2))
    return format_str