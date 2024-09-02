
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
    # append the numbers 0-1 to the number of bits (binary)
    if decimal < 0:
        raise ValueError("Invalid number")
    binary = bin(decimal)
    # remove the leading "0b"
    binary = binary[2:]
    # append the numbers 0-1 to the number of bits (binary)
    # the extra numbers are to help with the format
    bin_len = len(binary)
    if bin_len == 8:
        nums = ["0", "1"]
    elif bin_len == 16:
        nums = ["0", "1"] + ["db"]
    elif bin_len == 32:
        nums = ["0", "1", "db"]
    else:
        nums = ["0", "1", "db"] + ["0" for _ in range(32 - bin_len)]
    return "".join(nums[num] for num in binary)
