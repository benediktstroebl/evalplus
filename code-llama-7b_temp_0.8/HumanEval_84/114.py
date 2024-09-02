
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
    # 1) convert N into binary
    # 2) parse the binary number into its individual digits
    # 3) add each digit and return the total
    b_num = bin(N)
    b_num = b_num[2:]
    total = 0
    for digit in b_num:
        total = total + int(digit)
    return bin(total)

