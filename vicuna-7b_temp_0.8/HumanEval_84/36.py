
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
    # variable to store the binary representation
    binary_rep = str(N)

    # loop over each digit of the binary number
    for i in range(len(binary_rep)):
        # if the current digit is 0, add 100 to the previous binary number
        if binary_rep[i] == '0':
            binary_rep = binary_rep[:i] + binary_rep[i+1:] + str(100)
        else:
            # if the current digit is greater than 9, multiply the previous binary number
            if binary_rep[i] > '9':
                binary_rep = binary_rep[:i] + str(binary_rep[i-1] * 10) + binary_rep[i+1:]
            # if the current digit is 1, add 1 to the previous binary number
            elif binary_rep[i] == '1':
                binary_rep = binary_rep[:i] + str(1) + binary_rep[i+1:]

    return binary_rep
