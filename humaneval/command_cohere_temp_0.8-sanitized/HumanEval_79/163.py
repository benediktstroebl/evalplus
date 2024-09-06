def decimal_to_binary(decimal):
    # Initialize the result string with 'db' followed by enough '0's to handle any decimal
    result = 'db' + '0' * (decimal << 1)
    
    # Convert decimal to binary and adjust result
    for i in range(1, int(math.log(decimal, 2)) + 1):
        remainder = decimal % 2
        decimal //= 2
        result = str(remainder) + result
    
    # Append 'db' to the end of the result
    return result + 'db'
decimal = 15
result = decimal_to_binary(decimal)