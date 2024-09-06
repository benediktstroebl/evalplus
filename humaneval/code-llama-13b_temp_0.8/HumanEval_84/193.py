
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

    def to_binary(n):
        return (n > 0) and to_binary(n // 2) + str(n % 2) or ''
    
    binary_num = int(to_binary(N), 2)
    sum_of_digits = sum(int(digit) for digit in str(binary_num))
    return "1" if sum_of_digits % 2 == 0 else "0"
