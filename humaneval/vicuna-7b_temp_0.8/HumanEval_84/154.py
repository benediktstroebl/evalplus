
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
    # Check if the input is a positive integer within 0-10000
    if N >= 0 and N <= 10000:
        # Create a list of digits
        digits = [str(N)]
        while N != 0:
            if N % 10 == 0:
                digits.append(str(N // 10))
            N = N // 10
        return "".join(digits)
    else:
        return "Not a valid input"
