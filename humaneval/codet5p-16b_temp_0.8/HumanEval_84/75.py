
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

    bin_N = bin(N)[2:] #bin function returns the binary number of the input as a string. [2:] will remove the prefix '0b'
    return bin_N.replace("1","1 ").replace("0","1 ").strip() #replace all "1" with "1 " and then replace all "0" with "1 "
        
