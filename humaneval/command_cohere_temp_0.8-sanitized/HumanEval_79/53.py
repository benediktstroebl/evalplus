def decimal_to_binary(decimal):
    """Converts a decimal number to its binary representation."""
    bins = []
    while decimal:
        decimal, r = divmod(decimal, 2)
        bins.append(str(r))
    bins.reverse()
    return 'db' + ''.join(str(x) for x in bins) + 'db'