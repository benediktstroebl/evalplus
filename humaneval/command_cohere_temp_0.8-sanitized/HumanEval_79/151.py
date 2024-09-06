def decimal_to_binary(decimal):
    """Converts a decimal number to its binary representation with 0 and 1 chars."""
    import math
    result = "db" + "".join(["1" if math.fmod(decimal, 2) else "0" for _ in range(math.floor(decimal / 2))]) + "db"
    return result