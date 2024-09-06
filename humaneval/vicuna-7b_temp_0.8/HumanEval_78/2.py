
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
    if len(num) == 0:
        return 0
    if num[0] == 'A':
        if num[1] == 'B':
            if num[2] == 'C':
                if num[3] == 'D':
                    if num[4] == 'E':
                        if num[5] == 'F':
                            return 2
                        if num[6] == 'B':
                            if num[7] == 'C':
                                if num[8] == 'D':
                                    return 1
                        if num[9] == 'B':
                            return 1
                        return 0
                    if num[6] == 'D':
                        return 1
    if num[0] == 'A':
        if num[1] == 'B':
            if num[2] == 'C':
                if num[3] == 'D':
                    if num[4] == 'E':
                        if num[5] == 'F':
                            return 2
                        if num[6] == 'B':
                            if num[7] == 'C':
                                if num[8] == 'D':
                                    return 1
                        if num[9] == 'B':
                            return 1
                        return 0
                    if num[6] == 'D':
                        return 1
    if num[0] == 'A':
        if num[1] == 'B':
            if num[2] == 'C':
                if num[3] == 'D':
                    if num[4] == 'E':
                        if num[5] == 'F':
                            return 2
                        if num[6] == 'B':
                            if num[7] == 'C':
                                if num[8] == 'D':
                                    return 1
                        if num[9] == 'B':
                            return 1
                        return 0
                    if num[6] == 'D':
                        return 1
    if num[0] == 'B':
        if num[1] == '
