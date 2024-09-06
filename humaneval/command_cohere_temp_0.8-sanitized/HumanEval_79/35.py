def decimal_to_binary(decimal):
    """Convert a decimal number to binary format"""
    bib = []
    while decimal:
        bib.append(decimal % 2)
        decimal //= 2
    bib.reverse()
    return 'db' + ''.join(str(x) for x in bib) + 'db'