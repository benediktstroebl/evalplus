
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
    # return "0" if N == 0
    if N == 0:
        return "0"

    # convert N to binary string
    bin_str = str(bin(N))[2:]

    # create an empty list to store the sum of each digit
    total = []

    # loop through the binary string
    for i in bin_str:
        # add to the total the sum of each digit
        total.append(sum([int(x) for x in str(i)]))

    # join the total to a string and return it
    return ''.join([str(x) for x in total])
