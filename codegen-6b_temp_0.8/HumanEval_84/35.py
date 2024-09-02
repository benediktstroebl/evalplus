
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
    def helper(N):
        # Base Case
        if N == 0:
            return 0
        # Inductive Case
        else:
            N = helper(N // 10)
            # update accumulator
            return N + int(N % 10)
    # getting the helper to solve the problem
    return str(helper(N))
