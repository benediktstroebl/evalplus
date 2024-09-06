def decimal_to_binary(decimal):
    """Converts a decimal number to its binary representation."""
    bin_str = '{0:b}'.format(decimal)    # Convert decimal to binary and prefix with '0b'
    return 'db' + bin_str + 'db'           # Add 'db' prefixes and suffixes for better alignment
decimal = 15