
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
    
    # The following line of code gives us a string of the input number in binary.
    s = bin(N)[2:]

    # The following line of code gives us a list of string representations of the digits.
    binary_digits = [bin(int(d))[2:] for d in s]

    # The following line of code gives us a list of the integers represented by the
    # string representations of the digits in binary.
    # e.g. [1, 1, 0]
    # This could also be done with the following line of code:
    # binary_digits = [int(d, 2) for d in s]
    bin_digits_int = [int(d, 2) for d in binary_digits]

    # The following line of code sums the integers in the list.
    # e.g. [1, 1, 0] --> 1 + 1 + 0 = 2
    return ''.join([bin(sum(bin_digits_int))[2:]])
