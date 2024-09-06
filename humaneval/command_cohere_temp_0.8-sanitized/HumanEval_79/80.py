def decimal_to_binary(decimal):
    """Converts a decimal number to its binary representation, with extra '0's and '1's for formatting."""
    bins = []
    while decimal:
        decimal, r = divmod(decimal, 2)
        bins.append(str(r))
    bins.reverse()
    return 'db' + ''.join('1' if b else '0' for b in bins) + 'db'