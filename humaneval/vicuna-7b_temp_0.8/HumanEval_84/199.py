
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
    # Let's first convert the input N to a binary number
    binary_repr = str(N).zfill(base=2)
    # Then convert it back to an integer
    binary_value = int(binary_repr, 2)
    # Now we can calculate the sum of its digits by iterating over the digits
    # in the binary number and adding them up
    sum = 0
    for digit in binary_value:
        sum += digit
    return "1" + str(sum)