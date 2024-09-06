
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
    answer = []
    num = decimal
    while True:
        num, remainder = divmod(num, 2)
        answer.append(str(remainder))
        if num == 0:
            break
    answer.reverse()
    return "db" + "".join(answer) + "db"

