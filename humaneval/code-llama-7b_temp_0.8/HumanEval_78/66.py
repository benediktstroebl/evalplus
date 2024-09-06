
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
    HEX_TO_DEC = {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9, 'A': 10, 'B': 11, 'C': 12, 'D': 13, 'E': 14, 'F': 15}
    HEX_TO_DEC_REV = {v: k for k, v in HEX_TO_DEC.items()}
    if num:
        # convert from hexadecimal to decimal
        num_dec = 0
        for i in range(len(num)):
            num_dec += HEX_TO_DEC[num[i]]*16**(len(num)-i-1)

        # convert from decimal to hexadecimal
        num_hex = hex(num_dec)[2:]
        num_hex = num_hex.upper()
        if len(num_hex)%2 == 1:
            num_hex = '0'+num_hex

        # convert from hexadecimal to decimal
        num_dec_hex = 0
        for i in range(len(num_hex)):
            num_dec_hex += HEX_TO_DEC[num_hex[i]]*16**(len(num_hex)-i-1)
        
        # list of primes (the values are primes, the keys are hexadecimal equivalents)
        prime_list = {2: '2', 3: '3', 5: '5', 7: '7', 11: 'B', 13: 'D'}

        # list of all hexadecimal digits
        digits_list = [str(i) for i in range(16)]
        digits_list.append('A')
        digits_list.append('B')
        digits_list.append('C')
        digits_list.append('D')
        digits_list.append('E')
        digits_list.append('F')

        count =
