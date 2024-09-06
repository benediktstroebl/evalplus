
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

    binary_num = bin(N).replace("0b", "")
    binary_num = binary_num[::-1]
    result = ""
    s = 0
    for i in binary_num:
        if i == '1':
            s += 1
        else:
            result += str(s)
            s = 0
    result += str(s)
    return result[::-1]
    
