
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
    
    # [Explanation]
    #
    # Here is another example for N = 1000:
    #
    # binary of 1000 is 01110000 d1
    # sum of d1 is 1
    #
    # Here is another example for N = 150:
    #
    # binary of 150 is 00110110 d1 d2
    # sum of d1 is 1
    # sum of d2 is 5
    #
    # Here is another example for N = 147:
    #
    # binary of 147 is 00111001 d1 d2 d3
    # sum of d1 is 1
    # sum of d2 is 2
    # sum of d3 is 3
    
    binary = str(bin(N))
    binary = binary[2:]
    
    # binary is now "1" + "0"*(N-1)
    # binary = 011001...d1 ...d2...
    # (idle)
    # The first char is 1
    # The last char is 1 because N is odd.
    # (idle)
    # If N is even, then the last char will be 0
    
    # [Explanation]
    #
    # binary[:-1] will give the one char before the last char
    # binary[:-1] + "1" will give the one + "0"
    # binary[:-1] + "1" * (N/2) will give the one + "0" * (N/2)
    # binary[:-1] + "1" * (N/2) + "0" will give the one + "0" * (N/2) + "1"
    
    # (idle)
    # so we have the one +"0" + "0" + "1"
    # (idle)
    # now we have the one + "0" * (N/2) + "1"
    # (idle)
    # now we have the one + "0" + "0" + "1"
    # (idle)
    # now the last result is  "1"*(N/2) + "0"
    
    # binary = 011001...01