
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
    # the number of the bytes that needed to be encoded
    # the 1s bit is not counted
    n_bytes = (N.bit_length() - 1)//8 + 1
    # convert to binary string
    b = bin(N)[2:]
    # the number of the 0s
    n_0s = 8 * n_bytes - len(b)
    # fill in the 0s and sum the bits
    return bin(sum([int(x) for x in b + '0' * n_0s]))[2:]
