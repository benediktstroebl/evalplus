def decimal_to_binary(decimal):
    """Convert a decimal number to binary format."""
    bins = []
    while decimal:
        decimal, r = divmod(decimal, 2)
        bins.append(str(r))
    bins.reverse()
    return 'db' + ''.join(str(x) for x in bins) + 'db'