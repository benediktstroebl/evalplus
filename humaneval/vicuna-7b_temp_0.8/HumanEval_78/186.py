
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
    num = num.upper()
    if len(num) < 2:
        return 0
    else:
        count = 0
        for i in range(1, len(num)):
            if (num[i] == '2' or num[i] == '3' or num[i] == '5' or num[i] == '7' or num[i] == '11' or num[i] == '13' or num[i] == '17' or num[i] == '19' or num[i] == '23' or num[i] == '29' or num[i] == '31' or num[i] == '37' or num[i] == '41' or num[i] == '43' or num[i] == '47' or num[i] == '53' or num[i] == '59' or num[i] == '61' or num[i] == '67' or num[i] == '71' or num[i] == '73' or num[i] == '79' or num[i] == '83' or num[i] == '89' or num[i] == '97') and (num[i-1] != '2' or num[i-1] != '3' or num[i-1] != '5' or num[i-1] != '7' or num[i-1] != '11' or num[i-1] != '13' or num[i-1] != '17' or num[i-1] != '19' or num[i-1] != '23' or num[i-1] != '29' or num[i-1] != '31' or num[i-1] != '37' or num[i-1] != '41' or num[i-1] != '43' or num[i-1] != '47' or num[i-1] != '53' or num[i-1] != '59' or num[i-1] != '61' or num[i
