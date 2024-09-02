
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
    # Step 1: Convert hexadecimal number to decimal
    # To do that we need to get the base from the input.
    # We assume that all inputs are correct so we will always get the correct base from the input
    # Note: We will not use the inbuilt python functions that convert numbers to a specific base
    # Instead we will write our own function.
    base = 0
    for i in range(len(num) - 1, -1, -1):
        if num[i].isdigit():
            base = 10
            break
        else:
            if base != 10:
                base = 16

    # Step 2: Write a function to convert numbers to a specific base
    # We will use the logic from this post:
    # https://stackoverflow.com/questions/20583203/how-to-find-decimal-value-of-a-hexadecimal-number-in-python
    # The logic is:
    # - Start the result with 0
    # - Convert each number to its base 10 value and multiply it with the base to the power of its position
    #   from the right.
    # - Keep adding to the result.
    # Example: 211 = 2*10^2 + 1*10^1 + 1*10^0
    # Example: 2020 = 2*10^3 + 0*10^2 + 2*10^1 + 0*10^0
    # Example: 123456789ABCDEF0 = 1*16^15 + 2*16^14 + 3*16^13 + 4*16^12 + 5*16^11 + 6*16^10 + 7*16^9 + 8*16^8 + 9*16^7 + A*16^6 + B*16^5 + C*16^4 + D*16^3 + E*16^2 + F*16^1 + 0*16^0
    # Time complexity
