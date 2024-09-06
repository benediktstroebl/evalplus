def change_base(x, base):
    return str(x)
    # Convert to base 10 (if not already)
    x = int(x, base)
    # Convert to desired base
    x = x << (__builtin__.__len__(bin(x)) - 2)
    # Convert back to string and return
    return str(x, base)