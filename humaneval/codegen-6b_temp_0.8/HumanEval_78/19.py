
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
    
    # case when num is empty or is just a space
    if num == '' or num == ' ':
        return 0
        
    # case when num is just a single digit
    if len(num) == 1:
        return 1
        
    # list of primes
    primes = [2, 3, 5, 7, 11, 13, 17]
    
    # remove duplicates from num
    num_nospace = num.replace(' ', '')
    
    # add digits to num_nospace
    # num_nospace = 'ABED1A33'
    for i in range(len(num_nospace)):
        # add a digit to num_nospace
        for j in range(10):
            num_nospace += str(j)
            
            # create a new num_nospace by removing all digits that are in num
            # num_nospace = 'ABED1A3'
            for k in range(len(num)):
                if num_nospace[-1] == str(j):
                    if num_nospace[:-1] == num:
                        num_nospace = num_nospace[:-1]
                        break
    
    # binary to hexadecimal (capital letters are not required)
    hex_num = ''
    for n in range(len(num_nospace)):
        decimal = int(str(num_nospace[n]), 10)
        hex_num += str(decimal)
        
    # n_of_primes = 0
    # for n in range(len(hex_num)):
    #     for p in primes:
    #         if n % p == 0 and p != 2:
    #             n_of_primes += 1
    #             break
    #         elif n == len(hex_num) - 1:
    #             n_of_primes += 1

    # return n_of_primes
        
    primes_in_hex = 0
    for n in range(len(hex_num)):
        for p in primes:
            if n % p == 0 and p != 2:
                primes_in_hex +=