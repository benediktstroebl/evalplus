
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
        """
        Identifies a number prime?
        
        Args:
            n (int):
                number to be tested for primality
        
        Returns:
            boolean:
                True if number is prime, False if otherwise
        """
        if not isinstance(n, int):
            raise TypeError("%s is not an integer" % str(n))
        if n == 1:
            return False
        if n == 2 or n == 3:
            return True
        if n % 2 == 0 or n % 3 == 0:
            return False
        for i in range(5, int(math.ceil(math.sqrt(n))+1), 6):
            if n % i == 0 or n % (i+2) == 0:
                return False
        return True
    
    def count_digs(num):
        """
        Count number of digits in a number
        
        Args:
            num (int):
                number to be counted
        
        Returns:
            int:
                number of digits
        """
        if not isinstance(num, int):
            raise TypeError("%s is not an integer" % str(num))
        if num == 0:
            return 1
        return 1 + count_digs(num // 10)
    
    def next_digit(n):
        """
        Get the integer from the last digit
        
        Args:
            n (str):
                number to be processed
        
        Returns:
            int:
                the digit at the end of the string
        """
        return int(n[-1])
    
    def find_value(n):
        """
        Finds the value of the given number n
        
        Args:
            n (int):
                n to be found
        
        Returns:
            int:
                the value of the number
        """
        if n <= 0:
            return 0
        i = 1
        while True:
            if is_prime(i):
                if n % i == 0:
                    value = i
                    divisor = n // i
                    if divisor == i:
                        return