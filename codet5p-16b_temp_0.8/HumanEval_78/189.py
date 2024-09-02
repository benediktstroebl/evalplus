
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

    try:
        import math
        import re
        from collections import Counter
        
        def is_prime(num):
            if num == 1:
                return False
            if num == 2:
                return True
            if num % 2 == 0:
                return False
            for x in range(3, int(math.sqrt(num)) + 1, 2):
                if num % x == 0:
                    return False
            return True
        
        def num_of_primes(hex_num):
            num_of_primes = 0
            for key in hex_key_dict:
                if key in hex_num:
                    num_of_primes += hex_key_dict[key]
            return num_of_primes
        
        hex_num = re.sub('[^0-9A-F]', '', num.upper())
        hex_key_dict = {
            '2': 0,
            '3': 0,
            '5': 0,
            '7': 0,
            'B': 0,
            'D': 0
        }
