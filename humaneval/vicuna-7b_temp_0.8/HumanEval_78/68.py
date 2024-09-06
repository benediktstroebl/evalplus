
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
    # The input string is a hexadecimal number
    num = str(num)
    # You can use a dictionary to keep track of the numbers you've already checked
    # and to store the number of prime digits
    prime_digits = {}
    # You can use a list to keep track of the prime numbers (0-based)
    primes = []
    # You can use a list to keep track of the digits you've already checked
    # and to store the number of prime digits
    digits = []
    # You can use a while loop to iterate over the characters of the input string
    # and check if the character is a prime number
    for c in num:
        if c in primes:
            # If the character is already in the list of primes, you can skip it
            # If the character is 2,3,5,7,11,13,17,...
            if c in [2,3,5,7,11,13,17,31,37]:
                # If the character is a prime number, you can increment the counter
                # and append the digit to the list of digits
                if c in [2, 3, 5, 7, 11, 13, 17, 31, 37]:
                    digits.append(c)
                    prime_digits[c] += 1
            else:
                # If the character is not a prime number, you can skip it
                # and continue with the next iteration
                continue
        elif c in [0,1,4,6,9]:
            # If the character is 0,1,4,6,9
            # you can check if the character is a prime number
            if c in [2, 3, 5, 7, 11, 13, 17, 31, 37]:
                # If the character is a prime number, you can increment the counter
                # and append the digit to the list of digits
                digits.append(c)
                prime_digits[c] += 1
            else:
                # If the character is not a prime number, you can skip it
                # and
