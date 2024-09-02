
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
    # function to check if a digit is prime or not
    def is_prime(n):
        if n < 2:
            return False
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return False
        return True
    
    # function to check if a number is hexadecimal digit or prime
    def is_digit_or_prime(n):
        if n < 0 or n > 16:
            return False
        return (n in ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9", "A", "B", "C", "D", "E", "F"] or is_prime(int(n)))
    
    # check if input string is empty or not
    if len(num) == 0:
        return 0
    
    # check if input string is hexadecimal number
    if not any(c.isdigit() for c in num):
        return 0
    
    # convert input string to integer
    num = int(num, 16)
    
    # check if num is 0 or prime
    if num == 0 or is_prime(num):
        return 0
    
    # check if num is a hexadecimal digit
    if num in ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9", "A", "B", "C", "D", "E", "F"]:
        return 0
    
    # loop through all digits
    count = 0
    for i in range(num):
        # check if current digit is a prime
        if is_prime(num):
            count += 1
        else:
            # check if current digit is a hexadecimal digit
            if num == str(int(num)):
                count += 1
            else:
                # check if current digit is a hexadecimal digit
                if num == str(int(num) // 16):
                    count += 1
                elif num == str(int
