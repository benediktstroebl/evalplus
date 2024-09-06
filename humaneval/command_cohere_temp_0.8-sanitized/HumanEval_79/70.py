def decimal_to_binary(decimal):
    bin_str = bin(decimal)[2:]  # getting the binary representation without '0b'
    return "db" + bin_str + "db"