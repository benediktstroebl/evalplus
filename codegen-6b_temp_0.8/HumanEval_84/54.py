
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
    #Initialize result
    binary = ""
    
    #Implement the helper function here
    def helper(N, binary):
        if N == 0:
            return binary
        elif N % 2 == 0:
            return helper(N//2, binary+"0")
        else:
            return helper(N//2, binary+"1")
        
    return helper(N,binary)
