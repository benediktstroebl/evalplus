
def solve(N):
    """Given a positive integer N, return the total sum of its digits in binary.
    
    Example
        For N = 1000, the sum of digits will be 1 the output should be "1".
        For N = 150, the sum of digits will be 6 the output should be "110".
        For N = 147, the sum of digits will be 12 the output should be "1100".
    
    Variables:
        @N integer
             Constraints: 0 ≤ N ≤ 10000.
    Output:
         a string of binary number
    """
    def convert_binary(N):
        """Return the string representation of binary number str(N).
        
        Example
            For N = 1000, the output should be "1".
            For N = 150, the output should be "110".
            For N = 147, the output should be "1100".
        
        Args:
            N (int):  The integer number to convert to binary.
        Returns:
            A string of binary represenation 
        """
        return  str(bin(N))[2:]
    
    def convert_decimal(N):
        """Return the decimal number N.
        
        Args:
            N (str): The binary number to convert to decimal.
        Returns:
            A integer representing the decimal of binary.
        """
        return int(N,2)
    
    def convert_to_base_ten(num, base):
        """Return the decimal number num in base base.
        
        Args:
            num: the number to convert
            base: the base
        Returns:
            A decimal number
        """
        s = []
        while num > 0:
            s.append(str(num%base))
            num = num//base
        s.reverse()
        return ''.join(s)
    
    def convert_base_ten(num, base):
        """Return the decimal number num in base base.
        
        Args:
            num: the number to convert
            base: the base
        Returns:
            A decimal number
        """
        s = ''
        while num >= base:
            s += str(num%base)
            num //= base
        s += str(num)
        return s
    
    def is_perfect_square(N):
        """Return true if N is a perfect square, otherwise return false.
        
        Args:
            N (int): The integer to check.
        Returns:
            True if N is perfect square.
        """
        return int(N**0.5) ** 2 == N
    
    def is_perfect_square_neg(N):
        """Return true if N is a perfect square, otherwise return false.
        
        Args:
            N (