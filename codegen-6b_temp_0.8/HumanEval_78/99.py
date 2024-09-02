
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
    hex_primes = {'A':10, 'B':11, 'C':12, 'D':13, 'E':14, 'F':15}
    primes = [2, 3, 5, 7, 11, 13, 17]
    primes_dec = [11, 13]
    output = 0
    if num == '':
        return 0
    for i in range(len(num)):
        num_dec = int(num[i])
        if num_dec in primes_dec:
            output += 1
        else:
            i = 0
            while i < len(primes):
                j = 0
                while j < len(primes):
                    if primes[i] * primes[j] == num_dec:
                        output += 1
                    j += 1
                i += 1
    return output


import re
