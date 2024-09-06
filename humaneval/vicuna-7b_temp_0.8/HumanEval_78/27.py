
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
    # ascii code for digits
    digits = {
        '0': 58, '1': 59, '2': 60, '3': 61, '4': 62, '5': 63, '6': 64,
        '7': 65, '8': 66, '9': 67, 'A': 68, 'B': 71, 'C': 72, 'D': 73,
        'E': 74, 'F': 75, 'a': 97, 'b': 98, 'c': 99, 'd': 100, 'e': 101,
        'f': 102, 'g': 103, 'h': 104, 'i': 105, 'j': 106, 'k': 107, 'l': 108,
        'm': 109, 'n': 110, 'o': 111, 'p': 112, 'q': 113, 'r': 114, 's': 115,
        't': 116, 'u': 117, 'v': 118, 'w': 119, 'x': 120, 'y': 121, 'z': 122,
        '0': 48, '1': 49, '2': 50, '3': 51, '4': 52, '5': 53, '6': 54,
        '7': 55, '8': 56, '9': 57, 'A': 66, 'B': 72, 'C': 73, 'D': 74, 'E': 75,
        'F': 76, 'a': 97, 'b': 98, 'c': 99, 'd': 100, 'e': 101, 'f': 102,
        'g': 10
