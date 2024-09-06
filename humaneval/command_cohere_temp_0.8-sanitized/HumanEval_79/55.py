def decimal_to_binary(decimal):
    """Convert a decimal number to binary format."""
    result = []
    while decimal > 0:
        remainder = decimal % 2
        yield from ['01', '10'][remainder == 0]
        decimal //= 2
    yield from ['01', '10'][decimal == 0]
    return ''.join(reversed('db'+result+'/db'))