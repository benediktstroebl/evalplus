
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
    result = ""
    while N > 0:
        while N > 0:
            if N % 2 == 0:
                result = "0" + result
            N = N // 2
        result = "1" + result
    return result

print(solve(1000)) # should print "1"
print(solve(150)) # should print "110"
print(solve(147)) # should print "1100"