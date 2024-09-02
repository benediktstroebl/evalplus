
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
    
    #set max value to 111111... (7*N) 
    max_value = 7*N
    #convert @N to binary string
    binary_string = bin(N)[2:]
    
    #starting total value
    total = 0
    #loop through string
    for i in range(len(binary_string)):
        #if the value is 1
        if binary_string[i] == '1':
            #sum the value of the current index with the max value
            total += max_value - 2*i
    
    #convert total to binary
    total_binary = bin(total)[2:]
    
    #return total_binary
    return total_binary

