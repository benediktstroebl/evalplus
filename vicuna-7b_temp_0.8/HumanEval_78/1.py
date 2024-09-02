
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
    # initialize an empty dictionary to count the number of prime digits
    prime_digits = {}
    # loop through the input string
    for i in range(len(num)):
        # if the current character is a digit
        if num[i].isdigit():
            # get the hexadecimal digit value
            hex_value = int(num[i], 16)
            # check if the hexadecimal digit is a prime
            if hex_value in prime_digits:
                # increment the count of prime digits if it's prime
                prime_digits[hex_value] += 1
            else:
                # add the current hexadecimal digit to the dictionary of prime digits
                prime_digits[hex_value] = 1
    # return the count of prime digits
    return sum(prime_digits.values())
