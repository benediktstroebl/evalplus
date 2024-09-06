
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
    # The number of digits in the input string.
    num_digits = len(num)
    # A dictionary to count the number of prime digits.
    prime_count = {'2':0, '3':0, '5':0, '7':0, '11':0, '13':0, '17':0, '19':0, '23':0, '29':0, '31':0, '37':0, '41':0, '43':0, '47':0, '53':0, '59':0, '61':0, '67':0, '71':0, '73':0, '79':0, '83':0, '89':0, '97':0, '101':0, '103':0, '107':0, '109':0, '113':0, '127':0, '128':0, '131':0, '139':0, '149':0, '151':0, '163':0, '167':0, '173':0, '181':0, '193':0, '197':0, '199':0, '211':0, '223':0, '229':0, '233':0, '239':0, '249':0, '251':0, '257':0, '263':0, '269':0, '271':0, '277':0, '281':0, '289':0, '293':0, '307':0, '311':0, '313':0, '317':0, '331':0, '337':0, '347':0, '349':0, '353':0, '359':0, '367':0, '373':0, '383':0, '38
