def decimal_to_binary(decimal):
    """Returns binary string for given decimal number with extra 'db' chars"""
    res = ''
    while decimal:
        digit = decimal % 2
        res = str(digit) + res
        decimal //= 2
    return 'db' + res + 'db'