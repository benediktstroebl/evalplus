
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
        if num < 2:
            return False
        if num == 2:
            return True
        for i in range(2, int(num**0.5+1)):
            if num % i == 0:
                return False
        return True
    
    
    def count_digits(num):
        if num == '':
            return 0
        if num[0] == '0':
            return 0
        digits = {'0':0, '1':0, '2':0, '3':0, '4':0, '5':0, '6':0, '7':0, '8':0, '9':0, 'A':0, 'B':0, 'C':0, 'D':0, 'E':0, 'F':0}
        for digit in num:
            digits[digit] += 1
        return sum(digits.values())
    
    
    def find_primes(num):
        if num == '':
            return 0
        primes = []
        for i in range(ord('A'), ord('F')+1):
            if is_prime(i):
                primes.append(i)
        primes = set(primes)
        digits = {'0':0, '1':0, '2':0, '3':0, '4':0, '5':0, '6':0, '7':0, '8':0, '9':0, 'A':0, 'B':0, 'C':0, 'D':0, 'E':0, 'F':0}
        
        for digit in num:
            digit = ord(digit) - ord('A')
            if digit in primes:
                digits[digit] += 1
        final_count = 0
        for digit in digits.values():
            if digit == 2:
                final_count += 1
        return final_count
    
    return find_primes(num)
    

assert hex_key("1077E") == 2
assert hex_key("AB") == 1
assert hex_key("AED1A33") == 4
assert