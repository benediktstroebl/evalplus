
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
    if N > 10000 or N < 0:
        raise ValueError("N must be in range of 0 to 10000")

    binnary_number = bin(N)
    total_sum_of_digits = 0

    for digit in binnary_number:
        total_sum_of_digits += int(digit)

    return bin(total_sum_of_digits)[2:]

