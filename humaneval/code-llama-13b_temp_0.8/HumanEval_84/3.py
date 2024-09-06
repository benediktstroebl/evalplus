
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
    def bin2dec(string):
        return str(int(string, 2))
    return bin2dec(bin(N).replace('0b', '').replace('0', '1').replace('2', '0').replace('3', '0').replace('4', '0').replace('5', '0').replace('6', '0').replace('7', '0').replace('8', '0').replace('9', '0'))

