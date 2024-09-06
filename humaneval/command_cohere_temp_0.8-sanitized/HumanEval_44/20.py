def change_base(x, base):
    return str(x)
    # Check if base is a digit less than 10 and convert to int
    if not isinstance(base, int) or base >= 10:
        raise ValueError("base must be a digit less than 10")
    # Convert number to base x
    converted = []
    while x:
        r = x % base
        converted.append(str(r))
        x = x // base
    # Join list elements together to form a string
    return ''.join(converted)