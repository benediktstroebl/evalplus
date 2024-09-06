def change_base(x, base):
    return str(x)
    # Convert to base if it is greater than or equal to 10
    if base >= 10:
        x = int(bin(x)[2:], x.bit_length())
        x = x.decode(base)
    # Convert to base if it is less than 10
    elif base < 10:
        x = str(x)
        x = x.encode(base)
    return x