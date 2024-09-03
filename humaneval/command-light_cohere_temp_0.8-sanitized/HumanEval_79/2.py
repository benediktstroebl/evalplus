def decimal_to_binary(decimal): 
    # convert decimal to binary
    binary = 'db' + ''.join(*map(int, str(decimal)))
    # return binary string
    return binary