
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
    # N = N % 10 + 10 * solve(N // 10)
    # return N
    bin_num = str(bin(N))
    bin_num = bin_num[2:]
    # print(bin_num)
    total_sum = sum([int(i) for i in bin_num])
    # print(total_sum)
    return str(total_sum)
