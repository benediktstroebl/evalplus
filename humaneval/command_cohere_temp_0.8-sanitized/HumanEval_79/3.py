def decimal_to_binary(decimal):
    bin_str = bin(decimal)[2:]    
    return 'db' + bin_str + 'db'