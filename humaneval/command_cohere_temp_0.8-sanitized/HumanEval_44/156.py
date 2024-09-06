def change_base(x, base):
    return str(x)
    # Convert to base 10 (if not already)
    x = int(x, base)
    # Convert to new base value
    x = x.__mod__(base)
    # Convert back to string
    x = str(x)
    return x