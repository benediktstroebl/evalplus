def decimal_to_binary(decimal):
    binary_string = '{0:b}'.format(decimal)
    return 'db' + binary_string + 'db'
decimal = int(input("Enter a decimal number: "))