
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
        """Returns True if num is a prime number.
        >>> is_prime(2)
        True
        >>> is_prime(3)
        True
        >>> is_prime(5)
        True
        >>> is_prime(7)
        True
        """
        for d in range(2, int(num ** 0.5) + 1):
            if not num % d:
                return False
        return True

    def primes_up_to(n, primes):
        """Returns a list of primes numbers up to n
        >>> primes_up_to(10, [])
        [2,3,5,7]
        >>> primes_up_to(8, [2,3,5,7])
        [2,3,5,7]
        >>> primes_up_to(9, [2,3,5,7])
        [2,3,5,7]
        """
        return p[primes:n:primes]

    def decimal_to_binary(num):
        """translates a decimal number to a binary number"""
        num_str = str(num)
        if len(num_str) == 1:
            return str(num)
        else:
            return str(decimal_to_binary(int(num_str[:-1]))) + str(num_str[-1])

    def binary_to_decimal(num):
        """translates a binary number to a decimal number"""
        num2 = list(num)
        num2.reverse()
        digit = 0
        for d in num2:
            digit += int(d) * 2 ** digit
            digit -= 1
        return digit

    def is_hexadecimal_digit(num):
        """Returns True if num is a valid hexadecimal digit.
        >>> is_hexadecimal_digit(2)
        True
        >>> is_hexadecimal_digit(3)
        True
        >>> is_hexadecimal_digit(9)
        True
        >>> is_hexadecimal_digit(10)
        True
        >>> is_hexadec