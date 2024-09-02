
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
    def is_prime(num):
        if num <= 1:
            return False
        for i in range(2, num):
            if num % i == 0:
                return False
        return True

    def is_hex_digit(num):
        if num == '0' or num == '1' or num == '2' or num == '3' or \
        num == '4' or num == '5' or num == '6' or num == '7' or \
        num == '8' or num == '9' or num == 'A' or num == 'B' or \
        num == 'C' or num == 'D' or num == 'E' or num == 'F':
            return True

    def count_prime_digits(num):
        digits = len(num)
        count = 0
        for i in range(digits):
            if is_prime(int(num[i])):
                count += 1
        return count

    def count_digits(num):
        digits = len(num)
        count = 0
        for i in range(digits):
            if is_hex_digit(num[i]):
                count += 1
        return count

    def count_primes(num):
        digits = len(num)
        count = 0
        for i in range(digits):
            if is_prime(int(num[i])):
                count += 1
        return count

    def count_hex_digits(num):
        digits = len(num)
        count = 0
        for i in range(digits):
            if is_hex_digit(num[i]):
                count += 1
        return count

    # First we count the number of primes in the number
    primes = count_primes(num)
    # Then we count all the hexadecimal digits (and not primes)
    digits = count_digits(num)
    # Then we count the number of hexadecimal digits (not primes)
    hex_digits = count_hex_digits(num)
    return primes + digits - hex_digits

