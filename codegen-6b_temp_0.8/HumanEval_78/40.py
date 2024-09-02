
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
        """Returns True if num is a prime.
        Otherwise it returns False.
        """
        if num % 2 == 0 and num > 2:
            return False
        if num == 2:
            return True
        elif num % 2 == 0:
            return False
        i = 3
        while i * i <= num:
            if num % i == 0:
                return False
            i += 2
        return True
    
    def is_hex(num):
        if len(num) != 1 and not num.isdigit() or len(num) == 1 and not num.isalpha():
            return False
        if num.isdigit():
            return True
        return num.isalpha()

    def is_superprime(num):
        if is_prime(num):
            return is_prime(num + int(num))
        return False

    def get_decimal(num):
        return [int(x) for x in num]

    def is_greater(num):
        result = True
        try:
            for i in range(len(num) - 1):
                if num[i] > num[i + 1]:
                    result = True
                    break
                else:
                    result = False
            return result
        except:
            return result

    def is_supernum(num):
        if is_prime(int(num)):
            if is_prime(int(num) + int(num)) and is_prime(int(num)) and is_prime(int(num) + int(num) + int(num)):
                return True
        return False

    if not is_hex(num):
        return 0
    
    if is_supernum(num):
        return 4
    
    if not is_prime(int(num)):
        return 0

    return len(num) - get_decimal(num)[::-1].index(0) - 1
