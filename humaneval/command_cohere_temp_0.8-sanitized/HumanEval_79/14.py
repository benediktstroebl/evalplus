def decimal_to_binary(decimal):
    binary = bin(decimal)[2:]     # Convert decimal to binary and remove '0b'
    return f"db{binary}db"       # Add 'db' characters for better formatting
decimal = 15