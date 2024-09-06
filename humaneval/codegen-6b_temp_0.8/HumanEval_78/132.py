
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
    # since input is only digits and lower case letters and we are 
    # not interested in lower digits, we can use only upper letters.
    d = {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, 
         '8': 8, '9': 9, 'A': 10, 'B': 11, 'C': 12, 'D': 13, 'E': 14, 'F': 15}
    # we take only the first two characters of the number, 
    # compared with the digits 1 to 16, as they are the only ones that 
    # were used in the original problem.
    if num.isdigit() and 1 <= int(num[:2]) <= 16:
        # count the number of primes that were used
        primes = 0
        for i in range(2, int(num[:2])):
            # check if i is a prime or not
            if num[:2] == str(i) and str(i) in num[2:]:
                # if i is a prime, add 1 to primes
                primes += 1
        # if primes > 0, there can be two digits, A, B used
        if primes > 0:
            # since we already have A, B,
            # we can remove them from the total of primes
            # by subtracting them from the length of number string
            return len(num) - 2 - primes
        # else we can remove the first digit from the total of primes
        else:
            return len(num) - 1
    # else return 0, as we don't have a prime number
    return 0
