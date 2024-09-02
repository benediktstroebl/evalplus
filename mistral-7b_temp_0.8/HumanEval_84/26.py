
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
    # 123 = 1111101
    # N = 123
    # 1 = 00000001
    # 2 = 00000010
    # 3 = 00000011
    # 123 = 00000001 + 00000010 + 00000011
    # 1 + 2 + 3 = 6
    # 110 = 1 * 2 ** 2 + 0 * 2 ** 1 + 1 * 2 ** 0
    # 2 ** 0 = 1
    # 2 ** 1 = 2
    # 2 ** 2 = 4
    # 2 ** 3 = 8
    # 2 ** 4 = 16
    # 2 ** 5 = 32
    # 2 ** 6 = 64
    # 2 ** 7 = 128
    # 2 ** 8 =
