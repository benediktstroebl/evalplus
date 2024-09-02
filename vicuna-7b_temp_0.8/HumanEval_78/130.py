
def hex_key(num):
    """You have been tasked to write a function that receives 
    a hexadecimal number as a string and counts the number of hexadecimal 
    digits that are primes (prime number, or a prime, is a natural number 
    greater than 1 that is not a product of two smaller natural numbers).
    Hexadecimal digits are 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, A, B, C, D, E, F.
    Prime numbers are 2, 3, 5, 7, 11, 13, 17,...
    So you have to determine a number of the following digits: 2, 3, 5, 7, 
    B (=decimal 11), D (=decimal 13).
    Note: you may assume the input is always correct or empty string, 
    and symbols A,B,C,D,E,F are always uppercase.
    Examples:
    For num = "AB" the output should be 1.
    For num = "1077E" the output should be 2.
    For num = "ABED1A33" the output should be 4.
    For num = "123456789ABCDEF0" the output should be 6.
    For num = "2020" the output should be 2.
    """
    # Check if the input is empty
    if len(num) == 0:
        return 0
    # Check if the input is a single digit
    elif len(num) == 1:
        return 0
    # Check if the first digit is 0
    elif num[0] == '0':
        # Check if the number is 1
        if num[1] == '1':
            return 1
        # Check if the number is 2
        elif num[1] == '2':
            return 1
        # Check if the number is 3
        elif num[1] == '3':
            return 1
        # Check if the number is 4
        elif num[1] == '4':
            return 1
        # Check if the number is 5
        elif num[1] == '5':
            return 1
        # Check if the number is 6
        elif num[1] == '6':
            return 1
        # Check if the number is 7
        elif num[1] == '7':
            return 1
        # Check if the number is 8
        elif num[1] == '8':
            return 1
        # Check if the number is 9
        elif num[1] == '9':
            return 1
    # Check if the first digit is 1
    else:
        # Check if the number is 10
        if num[0] == '1':
            return 1
        # Check if the number is 11
        elif num[0] == '2':
            return 1
        # Check if the number is 12
        elif num[0] == '3':
            return 1
        # Check if the number is 13
        elif num[0] == '4':
            return 1
        # Check if the number is 14
        elif num[0] == '5':
            return 1
        # Check if the number is 15
        elif num[0] == '6':
            return 1
        # Check if the number is 16
        elif num[0] == '7':
            return 1
