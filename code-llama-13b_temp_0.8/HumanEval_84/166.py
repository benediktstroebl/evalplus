
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
    # The first solution:
    # return bin(N)[2:].count('1')
    # The second solution:
    #return bin(N).count('1')
    # The third solution:
    #return ''.join(bin(N).split('b')[1:]).count('1')
    # The fourth solution:
    # return bin(sum(map(int, bin(N)[2:])))[2:]
    # The fifth solution:
    # return str(sum(map(int, bin(N)[2:])))
    # The sixth solution:
    # return ''.join(str(bin(int(n) + int(n) + 1)) for n in str(N))[1:]
    # The seventh solution:
    # return ''.join(str(bin(int(n) + int(n) + 1))[3:] for n in str(N))
    # The eighth solution:
    # return ''.join(bin(int(n) + int(n) + 1)[3:] for n in str(N))
    # The ninth solution:
    # return ''.join(bin(int(n) + int(n) + 1)[-1:] for n in str(N))
    # The tenth solution:
    # return ''.join(bin(int(n) + int(n) + 1)[2:] for n in str(N))
    # The eleventh solution:
    # return ''.join(bin(int(n) + int(n) + 1)[3:] for n in str(N))
    # The twelth solution:
    # return ''.join(bin(int(n) + int(n) + 1)[3:] for n in str(N))
    # The thirteenth solution:
    # return ''.join(bin(int(n) + int(n) + 1)[3:] for n in str(N))
    # The fourteenth solution:
    # return ''.join(bin(int(n) + int(n) + 1)[3:] for n in str(N))
    # The fifteenth solution:
    # return ''.join(bin(
