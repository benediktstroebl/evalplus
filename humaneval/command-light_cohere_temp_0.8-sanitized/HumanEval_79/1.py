def decimal_to_binary(n):
    # Function to convert decimal to binary
    return "db" + bin(n)[2:].zfill() + "db"