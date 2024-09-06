def decimal_to_binary(decimal):
    """Converts a decimal number to its binary representation, with extra '0's and '1's for correctness"""
    decimal = str(decimal)
    binary  = '{}{}'.format(decimal, decimal)[::-1]
    return 'db' + binary + 'db'
decimal = 15