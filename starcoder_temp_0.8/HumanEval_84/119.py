
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
    def binary(n):
        # convert decimal number to binary number
        return bin(n)

    #code here
    binary_num = binary(N)
    binary_num = str(binary_num)
    binary_num = binary_num[2:]
    sum_of_digits = 0
    for digit in binary_num:
        sum_of_digits += int(digit)
    return sum_of_digits
