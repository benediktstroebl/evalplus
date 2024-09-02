
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
    # Initialize variables
    sum_digits = 0
    # Get sum of digits of N
    for char in str(N):
        sum_digits += int(char, 10)
    # Convert sum_digits to binary
    sum_digits = bin(sum_digits).replace("0b","")
    # return sum_digits
    return sum_digits

