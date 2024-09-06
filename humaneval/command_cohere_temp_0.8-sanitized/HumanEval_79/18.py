def decimal_to_binary(decimal):
    """Convert a decimal number to binary format."""
    bins = []
    while decimal > 0:
        remainder = decimal % 2
        decimal = decimal // 2
        bins.append(str(remainder))
    bins.reverse()
    return 'db' + ''.join(bins) + 'db'