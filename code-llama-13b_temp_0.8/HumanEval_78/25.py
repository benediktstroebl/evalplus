
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
    # Step 1: check if num is empty, return 0
    if num == '':
        return 0
    
    # Step 2: set a dictionary for prime numbers
    prime = {'2': True, '3': True, '5': True, '7': True, 
             'B': True, 'D': True}
    
    # Step 3: set counter to 0
    counter = 0
    
    # Step 4: loop over the number and count the prime numbers
    for i in range(len(num)):
        if num[i] in prime:
            counter += 1
    
    # Step 5: return the counter
    return counter

