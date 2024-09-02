
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
    #divide N by 2 and repeat until N = 0
    #if N is even, add 0 to the sum
    #if N is odd, add 1 to the sum
    
    #keep a running sum
    #if the running sum is greater than 9, add the sum to the running sum
    
    #loop through N and add each digit to running sum
    #until the sum is greater than 9, add the sum to the running sum
    #stop when N = 0
    
    #convert running sum to binary and return

    running_sum = 0
    while N > 0:
        #if N is even, add 0 to the sum
        if N % 2 == 0:
            running_sum += 0
        #if N is odd, add 1 to the sum
        else:
            running_sum += 1
        N = N // 2
    #convert running sum to binary
    output = bin(running_sum)
    #return output
    return output
