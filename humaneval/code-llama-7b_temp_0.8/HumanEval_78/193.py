
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
    # 2020, 1077E, AB, 123456789ABCDEF0, ABED1A33
    # 2020, 1077E, AB, 123456789ABCDEF0, ABED1A33
    hexdigits = "0123456789ABCDEF"
    hex_prime = "2357BDEF"
    hex_primes_dict = {d: 0 for d in hexdigits}
    num_primes = 0
    for i in range(len(num)):
        hex_primes_dict[num[i]] += 1
    for x in hex_primes_dict:
        if hex_primes_dict[x] != 0:
            if x in hex_prime:
                num_primes += hex_primes_dict[x]
            else:
                num_primes += hex_primes_dict[x] / 2
    return num_primes

