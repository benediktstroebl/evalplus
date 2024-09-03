def decimal_to_binary(decimal):
    """Convert a decimal number to binary format and return it as a string with 'db' wrappers.

    Parameters:
    decimal (int): Number to be converted to binary.

    Returns:
    str: Converted number in binary format with 'db' wrappers.
    """
    return "db" + bin(decimal)[2:] + "db"