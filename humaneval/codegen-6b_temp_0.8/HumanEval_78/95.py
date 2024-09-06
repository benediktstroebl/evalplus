
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
    def is_prime(n):
        """A simple method receives a number n and checks if n is a prime
        number or not by checking its divisibility by the numbers
        from 2 up to the square root of n. If it's true, then n is not
        a prime number, otherwise it's a prime number.
        If n is 1, then it's not a prime number.
        """
        if n == 1:
            return False
        for i in range(2, int(sqrt(n)) + 1):
            if n % i == 0:
                return False
        return True

    def check_digit(n):
        """For each hexadecimal digit in the number (a number of digits),
        you have to determine how many times the digit repeats itself,
        for example A repeats itself 3 times.
        For example:
        For an input number "1077E", the result should be 2,
        since B repeats itself three times, while D repeats itself once.
        """
        num = int(n, 16)
        count = 1
        while num:
            if num % 10 == num / 10:
                count += 1
            num //= 10
        return count

    if not num:
        return 0
    if not num.isupper():
        raise Exception("Error: string should be all uppercase!")
    if len(num) > 15:
        raise Exception("Error: string should be shorter than 16 letters!")
    if num.count('0') == len(num):
        raise Exception("Error: string should have at least one digit!")
    if not all(char in "0123456789ABCDEF" for char in num):
        raise Exception("Error: string should contain only hexadecimal digits!")
    if len(num) == 1:
        return 1
    return check_digit(num)

