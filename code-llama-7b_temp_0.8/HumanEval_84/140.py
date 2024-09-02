
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
    # list all digits of N in binary number
    num_bin = []
    while N != 0:
        remainder = N % 2
        num_bin.append(remainder)
        N = N // 2
    # find the sum of digits
    num_sum = 0
    for i in num_bin:
        num_sum += i
    # print the sum of digits in binary number
    num_sum_bin = []
    while num_sum != 0:
        remainder = num_sum % 2
        num_sum_bin.append(remainder)
        num_sum = num_sum // 2
    num_sum_bin.reverse()
    print(num_sum_bin)
    return "".join(map(str, num_sum_bin))
