def decimal_to_binary(decimal):
    """Converts a decimal number to its binary representation."""
    # Convert the decimal number to binary
    binary = bin(decimal)[2:]
    # Add leading zeros to make it 8 bits long
    binary = '0' * (8 - len(binary)) + binary
    # Add 'db' at the beginning and end for the specified format
    return 'db' + binary + 'db'