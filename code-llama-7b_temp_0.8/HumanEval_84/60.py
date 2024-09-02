
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
    # gets the decimal representation of N in a string.
    N_str = str(N)
    # print(N_str)
    # gets the list of digits in N_str.
    digits = [int(x) for x in N_str]
    # print(digits)
    total = 0
    for i in digits:
        # for each digit in N_str, gets the binary representation and
        # add the integer representation of each digit.
        total += bin(i).count("1")
    # convert the integer total to a string, and return the result.
    return str(total)
