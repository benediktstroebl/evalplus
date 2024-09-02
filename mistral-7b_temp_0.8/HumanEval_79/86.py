
def decimal_to_binary(decimal):
    """You will be given a number in decimal form and your task is to convert it to
    binary format. The function should return a string, with each character representing a binary
    number. Each character in the string will be '0' or '1'.

    There will be an extra couple of characters 'db' at the beginning and at the end of the string.
    The extra characters are there to help with the format.

    Examples:
    decimal_to_binary(15)   # returns "db1111db"
    decimal_to_binary(32)   # returns "db100000db"
    """
    # db_format_binary = ['db', '0', '1', 'db']
    # binary_num = 0
    # dec_num = decimal
    # binary = []
    # while dec_num > 0:
    #     binary_num = dec_num % 2
    #     dec_num = dec_num // 2
    #     binary.append(binary_num)
    # binary = binary[::-1]
    # for b in binary:
    #     print(db_format_binary[b], end='')
    # print()
    # return
    db_format_binary = ['db', '0', '1', 'db']
    binary = []
    decimal = decimal
    while decimal > 0:
        binary.append(decimal % 2)
        decimal //= 2
    binary = binary[::-1]
    for b in binary:
        print(db_format_binary[b], end='')
    print()
    return

