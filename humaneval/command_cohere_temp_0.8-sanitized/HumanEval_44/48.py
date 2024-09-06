def change_base(x, base):
    return str(x)
    # Convert to base 10 (if not already)
    x = int(x, base)
    # Convert to new base value
    x = x % base
    # Iterate through digits of x and create a new string
    result = []
    while x:
        result.append(str(x % base))
        x //= base
    # Reverse to ensure correct order
    result.reverse()
    # Return the string representation of the number in the new base
    return ''.join(result)