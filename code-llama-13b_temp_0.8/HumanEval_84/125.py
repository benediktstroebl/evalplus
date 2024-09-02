
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
    # Write your code here
    return format(N, 'b')
    bin_val = format(N, 'b')
    # check if odd or not
    if N % 2 == 0:
        bin_val = bin_val[:-1]
    else:
        bin_val = bin_val[1:]
    # for the next value, get the sum of digits
    sum = 0
    for val in bin_val:
        sum += int(val)
    return str(sum)

