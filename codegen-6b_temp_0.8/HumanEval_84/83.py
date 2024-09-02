
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
    
    # Initialize the final answer
    answer = "0" * N
    
    # Loop through the answer
    for i in range(len(answer)):
        
        # Get the current digit
        number = int(answer[len(answer) - 1 - i])
        
        # If the current digit is 1, add the current digit
        if number == 1:
            answer = answer[0:len(answer) - 1 - i] + "10"
            
        # If the current digit is 0, add the next digit
        else:
            answer = answer[0:len(answer) - 1 - i] + "110"
            
    # Return the answer for the function answer
    return answer
