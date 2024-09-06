
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
    num = num.replace('0','')
    num = num.replace('1','')
    num = num.replace('2','')
    num = num.replace('3','')
    num = num.replace('4','')
    num = num.replace('5','')
    num = num.replace('6','')
    num = num.replace('7','')
    num = num.replace('8','')
    num = num.replace('9','')
    num = num.replace('A','')
    num = num.replace('B','')
    num = num.replace('C','')
    num = num.replace('D','')
    num = num.replace('E','')
    num = num.replace('F','')
    prime = 0
    for i in num:
        if is_prime(int(i)):
            prime = prime + 1
    return prime

