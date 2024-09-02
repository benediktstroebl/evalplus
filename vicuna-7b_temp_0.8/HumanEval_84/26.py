
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
    # Write code here
    binary_form = str(N)
    while len(binary_form) > 0:
        if binary_form[0] == "0":
            binary_form = binary_form[1:]
            if len(binary_form) > 0:
                binary_form = binary_form[0] + binary_form
        else:
            binary_form = "1" + binary_form
        if len(binary_form) > 1:
            binary_form = binary_form[1:]
        if len(binary_form) > 0:
            binary_form = binary_form[0] + binary_form
    return binary_form
