
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
    b = str(bin(N)).split('b')[1]
    return ''.join([str(sum([int(i) for i in list(x)])) for x in [b[i:i+2] for i in range(0,len(b),2)]])
    """
    Alternative Solution:
    return str(sum([int(x) for x in str(bin(N))[2:]]))
    """
